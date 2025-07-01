from reportlab.pdfgen import canvas

lines = [
    "Engineering Handbook - Internal Use Only",
    "",
    "1. Engineering Onboarding",
    "- Complete onboarding in 7 business days.",
    "- GitHub, AWS, Slack, Linear setup required.",
    "- Mentor assigned for 30 days.",
    "",
    "2. Core Engineering Principles",
    "- Move fast, don’t break things (without tests)",
    "- Think product-first",
    "- Write code like it’ll be read in 10 years",
    "- Test coverage > 85%",
    "",
    "3. Deployment Process",
    "- Use main for prod releases",
    "- GitHub Actions + Grafana monitoring",
    "- Rollbacks in 15 mins if >5% fail",
    "- Postmortem for incidents",
    "",
    "4. Code Review Checklist",
    "1. Tests included?",
    "2. Logic modular?",
    "3. Comments actionable?",
    "4. Follows principles?",
    "",
    "5. Infra: Load Calculation",
    "Estimated Load = vCPU × average usage %",
    "Example: 16 × 0.65 = 10.4",
    "",
    "6. Version Control",
    "- Branch from main",
    "- Use: feat:, fix:, refactor:",
    "",
    "7. AI Systems",
    "- Uses OpenAI for tools",
    "- GPT-4o for all LLMs by Q4 2025"
]

c = canvas.Canvas("engineering_handbook.pdf")
y = 800
for line in lines:
    c.drawString(50, y, line)
    y -= 18
c.save()
