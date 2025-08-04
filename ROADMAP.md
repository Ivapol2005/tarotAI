# 🗺️ Tarot Insight AI Roadmap

## 🌟 Project Vision
An open-source playground for Tarot enthusiasts, developers, and data nerds. We combine:
- AI-powered card readings
- Anonymous research to explore "Do Scorpios really get The Death card more often?"
- Your choice of interface: CLI for coders, pretty web UI for everyone else.

## 🛠️ Phases

### ⌨️ Phase 0: Console Mode (MVP)
**Goal**: Core functionality for programmatic usage

- [ ] First have to choose API (maybe many) to use in program
- [ ] Implement base interpreter function:
    ```python
    def interpret_card(card: str, position: str, question: str = None) -> str:
        # Returns AI-generated interpretation**
    ```
- [ ] CLI interface:
    ```bash
    $ python tarot.py --card="The Moon" --position=reversed --question="Should I trust this opportunity?"
    ```

- [ ] Configuration:
    - [ ] Custom prompt templates
      
- [ ] Default tarot reading with celtic cross

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
