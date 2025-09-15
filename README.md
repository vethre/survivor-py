# Survivor-py

2D Survivor.io-like game на Python (Pygame).

## 🎮 Roadmap MVP (v0.1)
- [ ] Hero movement (WASD)
- [ ] Enemy spawn (basic square mob)
- [ ] Collision & HP bar
- [ ] XP orbs + Level up
- [ ] Upgrade choice UI (3 options)
- [ ] Game Over screen

## 🛠️ Tech stack
- Python 3.11+
- Pygame
- PyInstaller (сборки)

## 📂 Structure
game/
app.py
core/ # systems, rng, state
ui/ # hud, screens
assets/ # sprites, sounds
data/ # balance configs
tests/ # pytest

## 📌 Workflow
- Issues → Branch → Pull Request → Review → Merge
- `main` = релизы, `dev` = разработка, `feat/*` = отдельные фичи