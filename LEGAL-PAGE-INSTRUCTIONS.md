# Legal Page Instructions for All Wholelychit Websites

All Wholelychit websites and apps must include legal pages and footer links before public launch.

This applies to:
- Restaurants.ai
- ReadEasy30
- MathEasy30
- Petneeds.ai
- any future Wholelychit website or app

## Required Footer Links

Every website footer must include these links:

- Terms
- Privacy
- Advertising
- AI Disclaimer
- Community Rules

## Required Legal Pages

Each website should create a `/legal/` folder with these public pages:

- `/legal/terms.html`
- `/legal/privacy.html`
- `/legal/advertising.html`
- `/legal/ai-disclaimer.html`
- `/legal/community-rules.html`

## Master Source Documents

Use the shared templates stored here:

- `/legal/terms-of-service.md`
- `/legal/privacy-policy.md`
- `/legal/advertising-policy.md`
- `/legal/community-guidelines.md`
- `/legal/ai-disclaimer.md`

## Implementation Rule

Do not launch or promote any site publicly until the footer links are visible and the legal pages exist.

## Footer Example

```html
<footer class="site-footer">
  <nav aria-label="Legal links">
    <a href="legal/terms.html">Terms</a>
    <a href="legal/privacy.html">Privacy</a>
    <a href="legal/advertising.html">Advertising</a>
    <a href="legal/ai-disclaimer.html">AI Disclaimer</a>
    <a href="legal/community-rules.html">Community Rules</a>
  </nav>
</footer>
```

## Important Notes

- These pages reduce risk but do not eliminate all liability.
- Do not make guarantees about restaurants, food safety, allergy safety, reviews, prices, hours, or AI results.
- Use safe language such as "popular," "recommended," "community favorite," or "highly rated" instead of guaranteed claims.
- Payment data must be handled by Stripe, PayPal, or another trusted payment provider. Do not store credit card numbers directly.

## Codex / Developer Instruction

When updating any Wholelychit website, check whether legal footer links exist. If not, add them before adding new public features.
