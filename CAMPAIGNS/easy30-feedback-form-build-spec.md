# Easy30 Feedback Form Build Spec

Last updated: 2026-05-29

## Purpose

Plan a clean feedback and bug-report form for ReadEasy30 and MathEasy30 contact pages.

This is a build spec. Do not add a live form handler until the receiving email address, privacy language, spam settings, and platform choice are approved.

## Form goals

The form should collect helpful feedback without creating friction.

Best message types:

- idea or suggestion
- bug report
- happy note or success story
- worksheet request
- lesson request

## Recommended fields

### Role

Options:

- Parent / Guardian
- Teacher / Educator
- Adult Learner
- Tutor / Helper
- Other

### Message type

Options:

- Idea / Suggestion
- Bug Report
- Happy Note / Success Story
- Worksheet Request
- Lesson Request

### Message

Use one open text box.

Do not require phone number, address, child name, school name, or sensitive learner details.

## Safer button text

Use:

- Send Message
- Send Feedback
- Share Feedback

Avoid unless fully configured and verified:

- Send Securely
- Completely private
- HIPAA-safe
- Encrypted message

## Static-site form handler options

Possible options to review later:

- Formspree
- FormSubmit
- Netlify Forms if hosting supports it
- simple mailto link

## Privacy notes

Before launch:

- add clear privacy language near the form
- explain what information is collected
- avoid collecting student personal data
- avoid collecting medical, disability, or diagnosis details
- include contact email if needed
- test spam protection

## Suggested form copy

Heading:

Send Feedback

Intro:

Did you find a bug or have an idea for a reading or math lesson? Send a short note. Please do not include private student, medical, or school records.

## Build notes

- Use external CSS, not inline styles.
- Keep labels visible.
- Make fields large and mobile-friendly.
- Use strong contrast.
- Use a honeypot spam field if supported.
- Avoid disabling all spam controls until tested.
- Do not promise security features the form handler does not provide.

## Launch blocker

A live feedback form requires approval of:

- receiving email address
- form handler vendor
- privacy statement
- spam protection setting
- thank-you page or confirmation message
