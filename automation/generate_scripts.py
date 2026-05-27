"""
SlotsFreeUSA script generator

Reads video_scripts.json from the same folder, mixes script blocks, and writes
compiled plain-text scripts into ./compiled_scripts/.

Run:
    python generate_scripts.py

Optional:
    python generate_scripts.py --count 10
    python generate_scripts.py --json video_scripts.json --output compiled_scripts
"""

import argparse
import json
import random
import re
from datetime import datetime
from pathlib import Path

DEFAULT_JSON_FILE = "video_scripts.json"
DEFAULT_OUTPUT_DIR = "compiled_scripts"
DEFAULT_COUNT = 10

REQUIRED_DISCLOSURE_LINES = [
    "Text Overlay: 21+ Only. Terms Apply. Void where prohibited.",
    "Audio/Caption: This demo uses free-play virtual credits, not a real-money deposit.",
    "Footer: Play for entertainment. Set limits. Never chase losses.",
]

# Words and phrases that should be reviewed before publishing.
# These do not stop generation, but they mark a script as needing a human edit.
RISKY_TERMS = [
    "loophole",
    "guaranteed",
    "guarantee",
    "hidden trick",
    "wiping out",
    "pays out",
    "paying out",
    "cashout",
    "cash out",
    "replicate it",
    "without spending a dime",
    "no credit card required",
    "exclusive",
    "right now",
    "instant",
    "risk-free",
    "real casino odds exactly",
    "legal in forty-plus states",
    "stop wasting your real cash",
]


def load_json(json_path: Path) -> dict:
    """Load and validate the script source database."""
    if not json_path.exists():
        raise FileNotFoundError(
            f"System requires {json_path.name} to exist in the execution directory."
        )

    with json_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    try:
        scripts = data["scripts"]
        hooks = scripts["hooks"]
        mids = scripts["mid_sections"]
        ctas = scripts["calls_to_action"]
    except KeyError as exc:
        raise KeyError(f"Missing required JSON key: {exc}") from exc

    if not hooks or not mids or not ctas:
        raise ValueError("JSON database must include hooks, mid_sections, and calls_to_action.")

    return data


def slugify(value: str) -> str:
    """Create a safe filename piece."""
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "general"


def find_risky_terms(*text_blocks: str) -> list[str]:
    """Return risky terms found in selected blocks."""
    combined = " ".join(text_blocks).lower()
    found = []
    for term in RISKY_TERMS:
        if term.lower() in combined:
            found.append(term)
    return sorted(set(found))


def compatible_mid_sections(mids: list[dict], target_niche: str) -> list[dict]:
    """
    Prefer mid-sections that fit the hook niche.

    This keeps game-demo hooks with education/game mechanics,
    geo/sweepstakes hooks with compliance/transparency, and
    promo-code hooks with bonus/incentive content.
    """
    focus_map = {
        "game_demo": {"education", "game_mechanics", "value_proposition", "conversion_funnel"},
        "geo_sweepstakes": {"compliance", "transparency", "trust_building", "value_proposition"},
        "transactional_codes": {"bonus_details", "incentive", "transparency", "value_proposition"},
    }

    allowed_focuses = focus_map.get(target_niche, set())
    matches = [mid for mid in mids if mid.get("focus") in allowed_focuses]
    return matches or mids


def compile_script(batch_id: int, current_date: str, hook: dict, mid: dict, cta: dict) -> str:
    """Compile one plain-text production script."""
    risky_terms = find_risky_terms(
        hook.get("audio_voiceover", ""),
        hook.get("visual_prompt", ""),
        mid.get("audio_voiceover", ""),
        mid.get("visual_prompt", ""),
        cta.get("audio_voiceover", ""),
        cta.get("visual_prompt", ""),
    )

    risk_note = "PASS"
    if risky_terms:
        risk_note = "REVIEW NEEDED: " + ", ".join(risky_terms)

    lines = [
        "==================================================",
        "SLOTSFREEUSA DAILY MARKETING VIDEO SCRIPT",
        f"Batch ID: {batch_id} | Date Compiled: {current_date}",
        f"Target Niche Theme: {hook.get('target_niche', 'general').upper()}",
        f"Source Blocks: {hook.get('id', 'unknown')} + {mid.get('id', 'unknown')} + {cta.get('id', 'unknown')}",
        f"Compliance Scan: {risk_note}",
        "==================================================",
        "",
        "[0:00 - 0:10] HOOK STAGE",
        f"VISUAL: {hook.get('visual_prompt', '').strip()}",
        f"VOICEOVER: \"{hook.get('audio_voiceover', '').strip()}\"",
        "",
        "[0:10 - 0:45] VALUE MIDDLE STAGE",
        f"VISUAL: {mid.get('visual_prompt', '').strip()}",
        f"VOICEOVER: \"{mid.get('audio_voiceover', '').strip()}\"",
        "",
        "[0:45 - 0:60] CALL TO ACTION STAGE",
        f"VISUAL: {cta.get('visual_prompt', '').strip()}",
        f"VOICEOVER: \"{cta.get('audio_voiceover', '').strip()}\"",
        "",
        "--------------------------------------------------",
        "REQUIRED COMPLIANCE FOOTER:",
        *REQUIRED_DISCLOSURE_LINES,
        "",
        "FINAL HUMAN CHECK BEFORE POSTING:",
        "1. Remove or soften any risky wording marked above.",
        "2. Confirm all offers, terms, and locations are current before publishing.",
        "3. Use a clean website link, not raw tracking links, in social descriptions.",
        "4. Keep the video framed as adult entertainment education, not a promise of winnings.",
        "",
    ]

    return "\n".join(lines)


def load_and_compile_scripts(json_file_path: str, output_dir: str, count: int) -> None:
    """Load JSON database and generate compiled script text files."""
    json_path = Path(json_file_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    data = load_json(json_path)
    scripts = data["scripts"]
    hooks = scripts["hooks"]
    mids = scripts["mid_sections"]
    ctas = scripts["calls_to_action"]

    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"[+] Initializing compilation sequence for {current_date}...")
    print(f"[+] Output directory: {output_path.resolve()}")

    used_combinations = set()

    for batch_id in range(1, count + 1):
        selected_hook = random.choice(hooks)
        matched_mids = compatible_mid_sections(mids, selected_hook.get("target_niche", ""))
        selected_mid = random.choice(matched_mids)
        selected_cta = random.choice(ctas)

        combination_key = (
            selected_hook.get("id"),
            selected_mid.get("id"),
            selected_cta.get("id"),
        )

        # Try to avoid duplicates within the same generation run.
        attempts = 0
        while combination_key in used_combinations and attempts < 25:
            selected_hook = random.choice(hooks)
            matched_mids = compatible_mid_sections(mids, selected_hook.get("target_niche", ""))
            selected_mid = random.choice(matched_mids)
            selected_cta = random.choice(ctas)
            combination_key = (
                selected_hook.get("id"),
                selected_mid.get("id"),
                selected_cta.get("id"),
            )
            attempts += 1

        used_combinations.add(combination_key)

        niche = slugify(selected_hook.get("target_niche", "general"))
        file_name = output_path / f"slotsfreeusa_script_batch_ID{batch_id}_{niche}_{current_date}.txt"
        compiled_text = compile_script(
            batch_id=batch_id,
            current_date=current_date,
            hook=selected_hook,
            mid=selected_mid,
            cta=selected_cta,
        )

        file_name.write_text(compiled_text, encoding="utf-8")
        print(f" -> Compiled Asset: {file_name}")

    print("[+] Batch extraction complete. Review flagged wording before voiceover production.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate SlotsFreeUSA compiled video scripts.")
    parser.add_argument("--json", default=DEFAULT_JSON_FILE, help="Path to video_scripts.json")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_DIR, help="Output folder for compiled scripts")
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT, help="Number of scripts to generate")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    load_and_compile_scripts(args.json, args.output, args.count)
