# 🗺️ Tarot Insight AI Roadmap

## 🌟 Project Vision
An open-source playground for Tarot enthusiasts, developers, and data nerds. We combine:
- AI-powered card readings
- Anonymous research to explore "Do Scorpios really get The Death card more often?"
- Your choice of interface: CLI for coders, pretty web UI for everyone else.

## 🛠️ Phases

### ⌨️ Phase 0: Console Mode (MVP)
**Goal**: Core functionality for programmatic usage

- [X] First have to choose API (maybe many) to use in program
- [X] Implement base interpreter function:
    ```python
    def interpret_card(card: str, position: str, question: str = None) -> str:
        # Returns AI-generated interpretation**
    ```

    Text of prompt should look like this:
    ```Text
    give pls some advice based on my tarot fortune

    Spread: Celtic Cross
    ------------------------------
    1. The Past: King of Wands (Upright)
    2. The Future: The Star (Upright)
    3. Above: Nine of Swords (Upright)
    4. Below: Eight of Cups (Upright)
    5. The Present: The High Priestess (Upright)
    6. The Challenge: Ace of Wands (Upright)
    7. Advice: Four of Pentacles (Upright)
    8. External Influences: Wheel of Fortune (Upright)
    9. Hopes and/or Fears: Three of Cups (Upright)
    10. Outcome: Six of Pentacles (Upright)
    ```

- [X] CLI interface:
    ```bash
    $ python -c "tell(useReversed=True)"
    ```

- [X] Configuration:
    - [X] Custom tarot spreads

- [X] Default tarot reading with celtic cross

### 🌐 Phase 1: Web UI (v0.2)
**Goal**: User-friendly browser access

- [ ] Tech stack:
    - [ ] Frontend: Streamlit (fast prototype) → Next.js (production) ~~asked AI. don't know how to do frontend yet~~
    - [ ] Hosting

- [ ] Features:
    - [ ] Card selection visualizer
    - [ ] Reading history (localStorage)
    - [ ] API switcher

- [ ] Design

### 📊 Phase 2: Data & Research (v0.5)
**Goal**: Ethical data collection for astrological research

- [ ] Data consent flow:
      <p> ✅ 	<ins>I agree to share anonymous reading data</ins>
      <p> ✅ 	<ins>Include my birth (natal) chart info	</ins>

- [ ] Research metrics:
    | Metric          | Tracking Method         |
    |-----------------|-------------------------|
    | Card-Zodiac     | Chi-square test         |
    | Accuracy Rating | User feedback (1-5)     |

> [!IMPORTANT]
> Information should be secured

### 🔮 Phase 3: Full Ecosystem (v1.0)
**Goal**: Unified platform with advanced features

```mermaid
graph TD
    A[Console] --> C[Core Engine]
    B[Web UI] --> C
    C --> D[(Research Database)]
    D --> E[Public Dashboard]
