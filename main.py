import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. PAGE SETUP
# ==========================================
st.set_page_config(page_title="My Economics Study Hub", page_icon="📈", layout="wide")

# ==========================================
# 2. DESIGN TOKENS  (the "Ledger & Equilibrium" theme)
# ==========================================
# Palette -----------------------------------------------------------
INK        = "#0B1220"   # page background - deep ledger-ink navy
CARD       = "#141B2E"   # card panels
CARD_SOFT  = "#1B2540"   # hover / inset panels
BORDER     = "#263352"   # hairlines
GOLD       = "#E8B84B"   # primary accent - "equilibrium gold"
TEAL       = "#2DD4BF"   # secondary accent - elaboration / actual data
CORAL      = "#FF6B6B"   # tertiary accent - PYQ / recession marker
VIOLET     = "#A78BFA"   # quaternary accent - exercises
PAPER      = "#F5F3EE"   # primary text
MUTED      = "#8FA0BF"   # secondary text

# Fonts ---------------------------------------------------------------
FONT_IMPORT = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap"

CUSTOM_CSS = f"""
<style>
@import url('{FONT_IMPORT}');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: {INK};
    background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 28px 28px;
    color: {PAPER};
    font-family: 'Inter', sans-serif;
}}

[data-testid="stHeader"] {{ background-color: transparent; }}

/* ---- Sidebar: "Course Ledger" ---- */
[data-testid="stSidebar"] {{
    background-color: {CARD};
    border-right: 1px solid {BORDER};
}}
[data-testid="stSidebar"] * {{ color: {PAPER}; }}
.ledger-title {{
    font-family: 'Fraunces', serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: {GOLD};
    letter-spacing: 0.02em;
    margin-bottom: 0.1rem;
}}
.ledger-sub {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: {MUTED};
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 1.1rem;
}}
div[data-baseweb="select"] > div {{
    background-color: {CARD_SOFT} !important;
    border-color: {BORDER} !important;
    border-radius: 8px !important;
    color: {PAPER} !important;
}}

/* ---- Progress meter ---- */
.progress-wrap {{
    margin-top: 1.4rem;
    padding-top: 1.1rem;
    border-top: 1px dashed {BORDER};
}}
.progress-label {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: {MUTED};
    margin-bottom: 0.4rem;
}}
.progress-track {{
    width: 100%;
    height: 10px;
    background: {CARD_SOFT};
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid {BORDER};
}}
.progress-fill {{
    height: 100%;
    background: linear-gradient(90deg, {GOLD}, {TEAL});
    border-radius: 6px 0 0 6px;
}}
.progress-count {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: {GOLD};
    margin-top: 0.35rem;
}}
.study-tip {{
    margin-top: 1.1rem;
    font-size: 0.75rem;
    color: {MUTED};
    line-height: 1.4;
    font-style: italic;
}}

/* ---- Breadcrumb / dossier header ---- */
.breadcrumb {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: {MUTED};
    letter-spacing: 0.03em;
    margin-bottom: 0.3rem;
}}
.topic-title {{
    font-family: 'Fraunces', serif;
    font-weight: 700;
    font-size: 2.1rem;
    color: {PAPER};
    margin-bottom: 0.2rem;
    line-height: 1.15;
}}

/* ---- Equilibrium divider (the signature element) ---- */
.eq-divider {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.6rem 0 1.3rem 0;
}}
.eq-divider .line {{
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, {BORDER}, transparent);
}}
.eq-divider .diamond {{
    color: {GOLD};
    font-size: 0.9rem;
}}

/* ---- Content cards ---- */
.catch-card {{
    background: linear-gradient(135deg, {CARD_SOFT}, {CARD});
    border: 1px solid {BORDER};
    border-left: 4px solid {GOLD};
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 1rem;
}}
.catch-label {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: {GOLD};
    margin-bottom: 0.35rem;
}}
.catch-text {{
    font-size: 1.05rem;
    font-weight: 500;
    color: {PAPER};
    line-height: 1.55;
}}
.elab-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-left: 4px solid {TEAL};
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 1rem;
    font-size: 0.98rem;
    line-height: 1.7;
    color: {PAPER};
}}
.elab-card p {{ margin-bottom: 0.7rem; }}
.elab-card p:last-child {{ margin-bottom: 0; }}
.elab-label {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: {TEAL};
    margin-bottom: 0.5rem;
}}
.pyq-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-left: 4px solid {CORAL};
    border-radius: 10px;
    padding: 1rem 1.3rem;
    margin-bottom: 1rem;
    color: {PAPER};
    line-height: 1.6;
}}
.ex-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-left: 4px solid {VIOLET};
    border-radius: 10px;
    padding: 1rem 1.3rem;
    color: {PAPER};
    line-height: 1.6;
}}
.section-label {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.5rem;
}}

/* ---- graph frame ---- */
.graph-frame {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 10px;
    padding: 0.6rem 0.6rem 0.1rem 0.6rem;
    margin-bottom: 1.2rem;
}}

/* ---- mastery checkbox row ---- */
.stCheckbox {{ margin-top: 0.4rem; }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def eq_divider():
    """The signature element: a thin rule with a gold equilibrium diamond."""
    st.markdown(
        '<div class="eq-divider"><div class="line"></div>'
        '<div class="diamond">◆</div><div class="line"></div></div>',
        unsafe_allow_html=True,
    )


def render_explanation(text):
    """Splits the 'CATCH / ELABORATION' string into two styled cards."""
    catch_part, elab_part = "", text
    if "📖" in text:
        catch_part, elab_part = text.split("📖", 1)
    catch_part = catch_part.replace("📌", "").replace("**THE CATCH:**", "").strip()
    elab_part = elab_part.replace("**ELABORATION:**", "").strip()

    if catch_part:
        st.markdown(
            f'<div class="catch-card"><div class="catch-label">📌 The Catch</div>'
            f'<div class="catch-text">{catch_part}</div></div>',
            unsafe_allow_html=True,
        )

    paragraphs = "".join(f"<p>{p.strip()}</p>" for p in elab_part.split("\n\n") if p.strip())
    st.markdown(
        f'<div class="elab-card"><div class="elab-label">📖 Elaboration</div>{paragraphs}</div>',
        unsafe_allow_html=True,
    )


# ==========================================
# 3. MATPLOTLIB THEME (matches the app)
# ==========================================
def style_axes(ax, fig):
    fig.patch.set_facecolor(CARD)
    ax.set_facecolor(CARD)
    for spine in ax.spines.values():
        spine.set_color(BORDER)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.xaxis.label.set_color(PAPER)
    ax.yaxis.label.set_color(PAPER)
    ax.title.set_color(PAPER)
    ax.grid(color=BORDER, linestyle="--", linewidth=0.6, alpha=0.5)
    legend = ax.get_legend()
    if legend:
        legend.get_frame().set_facecolor(CARD_SOFT)
        legend.get_frame().set_edgecolor(BORDER)
        for text in legend.get_texts():
            text.set_color(PAPER)


# ==========================================
# 4. THE DATABASE (Your Digital Filing Cabinet)
# ==========================================
database = {
    "Advanced Microeconomics": {
        "Chapter 1: Technology": {
            "Topic: Production Possibilities & Isoquants": {
                "graph": "isoquant",
                "explanation": "📌 **THE CATCH:** A business takes inputs like labor and machines to create outputs. An isoquant is a curve showing all the different input recipes to make the exact same amount of output.\n\n📖 **ELABORATION:** A production possibilities set describes all the realistic combinations of inputs and outputs a business can technologically use.\n\nThe curve that shows equal-output combinations is called an isoquant. The slope of this curve is called the Technical Rate of Substitution (TRS). It tells us exactly how much of one input the factory has to give up to use a little more of another input, all while keeping the final output perfectly constant.",
                "pyq": "Define the Technical Rate of Substitution and explain its geometric meaning.",
                "exercise": "Review the difference between Cobb-Douglas and Leontief technology.",
            },
            "Topic: Returns to Scale": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** Returns to scale tells us what happens to our output when we multiply all our inputs by the same amount.\n\n📖 **ELABORATION:** If doubling all your factory inputs gives you exactly double the output, that is called constant returns to scale. If output increases more than the scale of your inputs, it is called increasing returns to scale.\n\nIf the output increases less than your inputs, it is decreasing returns to scale. The elasticity of scale measures the exact percentage increase in output caused by a one percent increase in all inputs.",
                "pyq": "Explain the difference between increasing and decreasing returns to scale.",
                "exercise": "Calculate returns to scale for the CES production function where rho = 1.",
            },
        },
        "Chapter 2: Profit Maximization": {
            "Topic: Maximizing Profits": {
                "graph": "profit_max",
                "explanation": "📌 **THE CATCH:** To make the highest profit, the money earned from making one extra item must exactly equal the cost of making it.\n\n📖 **ELABORATION:** Economic profit is the revenue a business receives minus all the economic costs it incurs. A competitive firm cannot change market prices, so it only decides how much to produce.\n\nTo find the maximum profit, we use an 'isoprofit line'. This line shows all the combinations of inputs and outputs that give the exact same profit amount. On a graph, the absolute maximum profit happens exactly where the curve of the production function touches the isoprofit line.",
                "pyq": "Explain why a profit-maximizing firm will choose an input level where the isoprofit line is tangent to the production function.",
                "exercise": "Calculate the profit function for a simple Cobb-Douglas technology.",
            }
        },
        "Chapter 7: Utility Maximization": {
            "Topic: Getting the Most Happiness": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** People have a limited budget and shop to find the bundle of goods that brings them the highest possible satisfaction.\n\n📖 **ELABORATION:** Consumers want to maximize their utility, which is just a fancy word for satisfaction. The expenditure function is a tool that tells us the absolute minimum amount of money a person needs to reach a specific level of happiness at current prices.\n\nRoy's Identity and Shephard's Lemma are mathematical shortcuts that let us instantly find a consumer's demand for a good just by looking at these utility and expenditure formulas.",
                "pyq": "State and prove Roy's identity and explain its usefulness.",
                "exercise": "Find the expenditure function for the Cobb-Douglas utility function.",
            }
        },
        "Chapter 8: Choice": {
            "Topic: The Slutsky Equation": {
                "graph": "slutsky",
                "explanation": "📌 **THE CATCH:** When a price drops, you buy more for two reasons: the item is now a better deal than others, and your leftover money acts like a bonus paycheck.\n\n📖 **ELABORATION:** The Slutsky equation is a mathematical formula that splits a person's reaction to a price change into two separate pieces. The first piece is the Substitution Effect: you naturally swap more expensive goods for the cheaper good.\n\nThe second piece is the Income Effect: because the good is cheaper, you have more purchasing power left over, which feels like getting a raise. The total change in your demand is the sum of these two effects.",
                "pyq": "Use the Slutsky equation to decompose a price change into substitution and income effects.",
                "exercise": "Draw the Hicks and Slutsky compensation bounds for a price increase.",
            },
            "Topic: Revealed Preference": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** We can figure out what a person likes just by watching what they choose to buy in the store.\n\n📖 **ELABORATION:** Revealed preference analyzes observable variables to see if consumers are making rational choices. The Generalized Axiom of Revealed Preference (GARP) states that if bundle A is revealed to be preferred to bundle B, bundle B cannot be strictly preferred to A.\n\nIf a person's shopping data is consistent with GARP, there exists a utility function that perfectly explains their behavior.",
                "pyq": "No previous questions recorded yet.",
                "exercise": "Review the differences between WARP, SARP, and GARP.",
            },
        },
    },

    # ------------------------------------------------------------------
    # ADVANCED MACROECONOMICS -- Chapter 10 fully built out
    # ------------------------------------------------------------------
    "Advanced Macroeconomics": {
        "Chapter 10: Economic Fluctuations": {
            "Topic: The Business Cycle & GDP Fluctuations": {
                "graph": "business_cycle",
                "explanation": (
                    "📌 **THE CATCH:** The economy never grows in a perfectly straight line — it moves up and down "
                    "like waves, and economists call these ups and downs the business cycle.\n\n"
                    "📖 **ELABORATION:** GDP is simply the total value of everything a country produces in a year — "
                    "think of it as the country's total paycheck. That paycheck does not grow smoothly every single "
                    "year. Sometimes it grows quickly, which we call an expansion or a boom. Sometimes it actually "
                    "shrinks for a while, which we call a recession.\n\n"
                    "On a graph, the highest point right before things start turning bad is called a peak, and the "
                    "lowest point right before things start improving again is called a trough. Actual real GDP "
                    "wobbles above and below the economy's long-run trend line, which is the smooth, steady growth "
                    "path the economy would follow if nothing ever went wrong.\n\n"
                    "One important thing to remember for exams: business cycles are irregular. They do not repeat "
                    "on a fixed schedule like the seasons of the year. Some expansions last many years, some "
                    "recessions last only a few months, and nobody can predict the exact timing in advance."
                ),
                "pyq": "Explain the meaning of a business cycle and identify its main phases with the help of a diagram.",
                "exercise": "Using the graph shown, label which sections you think represent a recession and which represent an expansion, and justify your answer in two sentences.",
            },
            "Topic: Okun's Law - Linking GDP to Jobs": {
                "graph": "okun_law",
                "explanation": (
                    "📌 **THE CATCH:** Okun's Law is a simple rule of thumb that connects how fast the economy grows "
                    "to how many people find or lose jobs.\n\n"
                    "📖 **ELABORATION:** The rule says that when GDP grows faster than its normal rate, unemployment "
                    "tends to fall, and when GDP grows slower than normal, unemployment tends to rise. As a rough "
                    "guide, for every extra one percentage point that GDP growth is above its usual pace, the "
                    "unemployment rate tends to fall by about half a percentage point.\n\n"
                    "This rule is useful because it lets economists make a quick, educated guess about what is "
                    "happening in the job market just by looking at the newest GDP growth figures, without waiting "
                    "for fresh unemployment surveys to come out.\n\n"
                    "It is important to remember that Okun's Law is a statistical pattern discovered by the "
                    "economist Arthur Okun, not a fixed law of physics. The exact numbers can be a little different "
                    "across different countries and different time periods, so it should be treated as a helpful "
                    "approximation rather than an exact formula."
                ),
                "pyq": "State Okun's Law and explain what it tells us about the relationship between output and unemployment.",
                "exercise": "If a country's GDP grows two percentage points faster than its usual rate this year, use Okun's rule of thumb to estimate the likely change in the unemployment rate.",
            },
            "Topic: Time Horizons - Short Run vs Long Run": {
                "graph": "none",
                "explanation": (
                    "📌 **THE CATCH:** In economics, 'long run' does not simply mean far in the future — it means "
                    "enough time has passed for prices to fully adjust. The 'short run' is the messier period "
                    "before that full adjustment happens.\n\n"
                    "📖 **ELABORATION:** The classical model of the economy, which most of introductory economics is "
                    "built on, assumes that prices adjust immediately to keep supply and demand in balance. This "
                    "assumption works reasonably well when we look at the economy over many years — the long run.\n\n"
                    "But in the short run, many prices are 'sticky'. Shops do not reprint their menus every single "
                    "day, workers' wages are often fixed by a contract for a year or more, and many business deals "
                    "are agreed upon in advance. Because these prices cannot adjust instantly, the economy cannot "
                    "immediately settle back into its ideal balance when something changes.\n\n"
                    "This stickiness is the whole reason economic fluctuations exist at all. Because prices are "
                    "slow to move in the short run, a change in demand or in the money supply can actually change "
                    "how much is produced and how many people have jobs, not just change prices. This is exactly "
                    "why economists built a separate model — the Aggregate Demand and Aggregate Supply model — just "
                    "to study these short-run wiggles."
                ),
                "pyq": "Explain why the classical dichotomy does not hold in the short run.",
                "exercise": "Give two real-world examples of prices that are 'sticky' and explain why they cannot adjust quickly.",
            },
            "Topic: The Aggregate Demand Curve": {
                "graph": "ad_curve",
                "explanation": (
                    "📌 **THE CATCH:** The Aggregate Demand curve simply shows that the cheaper the overall price "
                    "level of a country's goods, the more everyone together wants to buy.\n\n"
                    "📖 **ELABORATION:** Aggregate demand is the total quantity of goods and services that "
                    "households, businesses, the government, and foreign buyers all want to purchase at each "
                    "possible overall price level. On the graph, the price level sits on the vertical axis and "
                    "total output sits on the horizontal axis, and the curve slopes downward.\n\n"
                    "There are three simple reasons for this downward slope. First, the wealth effect: when prices "
                    "fall, the money you already have in savings can buy more, so you feel richer and spend more. "
                    "Second, the interest-rate effect: when prices fall, people need to keep less cash on hand for "
                    "daily shopping, so they lend out the extra cash, which pushes interest rates down and "
                    "encourages businesses to invest more. Third, the exchange-rate effect: when domestic prices "
                    "fall, the country's goods become cheaper for foreigners, so exports rise.\n\n"
                    "One key exam point: moving along this curve only happens because the price level itself "
                    "changed. If something else changes, like government spending or foreign incomes, the entire "
                    "curve shifts to a new position instead — and that is a completely different event, covered in "
                    "the shocks topic."
                ),
                "pyq": "Explain the three effects that cause the aggregate demand curve to slope downward.",
                "exercise": "Distinguish between a movement along the AD curve and a shift of the AD curve, giving one example of each.",
            },
            "Topic: Aggregate Supply - Short Run vs Long Run": {
                "graph": "as_curves",
                "explanation": (
                    "📌 **THE CATCH:** In the long run, the economy always produces its 'natural' full-employment "
                    "output no matter what prices do — but in the short run, higher prices can actually coax "
                    "businesses into producing more.\n\n"
                    "📖 **ELABORATION:** The long-run aggregate supply curve, or LRAS, is drawn as a straight "
                    "vertical line at the economy's natural level of output. It is vertical because, over the long "
                    "run, how much an economy can produce depends only on real things — the number of workers, the "
                    "amount of machinery and buildings, and the level of technology — and not on the overall price "
                    "level at all. This is the classical dichotomy at work again.\n\n"
                    "The short-run aggregate supply curve, or SRAS, is drawn sloping upward instead. Because wages "
                    "and some prices are sticky in the short run, when the overall price level rises unexpectedly, "
                    "individual businesses find they can sell their output at a relatively better price for a "
                    "while, so they choose to produce more. Economists use a few different theories, such as sticky "
                    "wages, sticky prices, and misperceptions about prices, to explain this — but the simplest way "
                    "to remember it is that firms temporarily produce more when prices surprise them on the "
                    "upside.\n\n"
                    "On the graph, think of the LRAS as a permanent wall that output cannot pass in the long run, "
                    "while the SRAS is a temporary hill that can shift the economy above or below that wall for a "
                    "while."
                ),
                "pyq": "Explain why the long-run aggregate supply curve is vertical while the short-run aggregate supply curve slopes upward.",
                "exercise": "Name the three theories economists use to explain the upward slope of the short-run aggregate supply curve.",
            },
            "Topic: Demand and Supply Shocks": {
                "graph": "demand_shock",
                "explanation": (
                    "📌 **THE CATCH:** A 'shock' is any sudden event that pushes the AD or the AS curve to a new "
                    "spot, and depending on which curve moves, prices and output can rise together, fall together, "
                    "or move in opposite directions.\n\n"
                    "📖 **ELABORATION:** A shock is simply an unexpected event or policy change — such as a jump in "
                    "government spending, a stock market crash, or a sudden rise in oil prices — that shifts either "
                    "the AD curve or the AS curve to a new position, rather than just moving the economy along an "
                    "existing curve.\n\n"
                    "Take a positive demand shock as the main example, caused perhaps by a rise in government "
                    "spending or an export boom. This shifts the entire AD curve to the right. In the short run, "
                    "both the price level and total output rise above the natural level, because the SRAS curve is "
                    "still upward sloping at that point. Over time, as sticky wages and prices slowly adjust "
                    "upward, output drifts back down to its original natural level, but the economy now settles at "
                    "a permanently higher price level.\n\n"
                    "A negative demand shock works exactly in reverse: both output and prices fall in the short "
                    "run. Supply shocks behave differently — for example, a sudden oil price spike shifts the SRAS "
                    "curve to the left, pushing prices up while output falls at the same time. This unusual "
                    "combination of rising prices and falling output has a special name: stagflation."
                ),
                "pyq": "Using the AD-AS diagram, show and explain the short-run and long-run effects of an increase in government spending.",
                "exercise": "Explain what 'stagflation' means and which curve shift typically causes it.",
            },
        }
    },

    "Research Methodology": {
        "Module 1: Foundations": {
            "Topic 1: Introduction to Research": {
                "graph": "none",
                "explanation": "Type your notes from Siratul Mustaquim here.",
                "pyq": "Add questions here.",
                "exercise": "Add exercises here.",
            }
        }
    },
    "Environmental Economics": {},
    "Monetary Economics": {},
}


# ==========================================
# 5. THE GRAPHING ENGINE
# ==========================================
def draw_graph(graph_type):
    fig, ax = plt.subplots(figsize=(6.2, 4))

    if graph_type == "isoquant":
        x = np.linspace(0.5, 10, 100)
        y = 10 / x
        ax.plot(x, y, color=GOLD, linewidth=3)
        ax.set_title("Isoquant Curve", fontsize=12, fontweight="bold")
        ax.set_xlabel("Factor 1")
        ax.set_ylabel("Factor 2")

    elif graph_type == "profit_max":
        x_prod = np.linspace(0, 10, 100)
        y_prod = np.sqrt(x_prod) * 3
        x_profit = np.linspace(0, 10, 100)
        y_profit = 0.5 * x_profit + 2.25
        ax.plot(x_prod, y_prod, color=TEAL, linewidth=3, label="Production Curve")
        ax.plot(x_profit, y_profit, color=GOLD, linewidth=2, linestyle="--", label="Isoprofit Line")
        ax.plot(4.5, np.sqrt(4.5) * 3, "o", color=CORAL, markersize=8)
        ax.set_title("Profit Maximization Point", fontsize=12, fontweight="bold")
        ax.set_xlabel("Input Amount")
        ax.set_ylabel("Output Amount")
        ax.legend()

    elif graph_type == "slutsky":
        x_indiff = np.linspace(1, 10, 100)
        y_indiff1 = 12 / x_indiff
        y_indiff2 = 20 / x_indiff
        ax.plot(x_indiff, y_indiff1, color=GOLD, linewidth=2, label="Old Utility")
        ax.plot(x_indiff, y_indiff2, color=TEAL, linewidth=2, label="New Utility")
        ax.plot([0, 8], [8, 0], color=MUTED, linewidth=1.5, label="Old Budget")
        ax.plot([0, 12], [8, 0], color=CORAL, linewidth=1.5, label="New Budget")
        ax.set_title("Substitution & Income Effects", fontsize=12, fontweight="bold")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.legend()

    elif graph_type == "business_cycle":
        t = np.linspace(0, 20, 500)
        trend = 100 + 3.2 * t
        cycle = 9 * np.sin(0.7 * t)
        actual = trend + cycle
        ax.fill_between(t, actual, trend, where=(actual < trend), color=CORAL, alpha=0.18, label="Recession")
        ax.fill_between(t, actual, trend, where=(actual >= trend), color=TEAL, alpha=0.15, label="Expansion")
        ax.plot(t, trend, color=MUTED, linestyle="--", linewidth=1.5, label="Potential GDP (trend)")
        ax.plot(t, actual, color=GOLD, linewidth=2.5, label="Actual GDP")
        ax.set_title("The Business Cycle", fontsize=12, fontweight="bold")
        ax.set_xlabel("Years")
        ax.set_ylabel("Real GDP")
        ax.legend(fontsize=8, loc="upper left")

    elif graph_type == "okun_law":
        rng = np.random.default_rng(7)
        gdp_growth = rng.uniform(-2, 8, 40)
        unemployment_change = -0.5 * (gdp_growth - 3) + rng.normal(0, 0.6, 40)
        line_x = np.linspace(-2, 8, 50)
        line_y = -0.5 * (line_x - 3)
        ax.scatter(gdp_growth, unemployment_change, color=TEAL, alpha=0.75, s=35, label="Observed years")
        ax.plot(line_x, line_y, color=GOLD, linewidth=2.5, linestyle="--", label="Okun's Law trend")
        ax.axhline(0, color=BORDER, linewidth=1)
        ax.set_title("Okun's Law: Growth vs Unemployment", fontsize=12, fontweight="bold")
        ax.set_xlabel("GDP Growth Rate (%)")
        ax.set_ylabel("Change in Unemployment (pp)")
        ax.legend(fontsize=8)

    elif graph_type == "ad_curve":
        # Straight-line AD: P = 8.4 - 0.09*Y, kept linear so marker points sit exactly on it.
        y = np.linspace(20, 90, 100)
        p = 8.4 - 0.09 * y
        ax.plot(y, p, color=GOLD, linewidth=3, label="Aggregate Demand (AD)")
        for yv in [30, 80]:
            pv = 8.4 - 0.09 * yv
            ax.plot(yv, pv, "o", color=CORAL, markersize=7)
        y_hi, p_hi = 30, 8.4 - 0.09 * 30
        y_lo, p_lo = 80, 8.4 - 0.09 * 80
        ax.annotate("", xy=(y_lo, p_lo), xytext=(y_hi, p_hi),
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.4))
        ax.text((y_hi + y_lo) / 2 - 8, (p_hi + p_lo) / 2 + 0.4,
                "Lower price →\nmove along the\nsame AD curve", color=PAPER, fontsize=8)
        ax.set_title("The Aggregate Demand Curve", fontsize=12, fontweight="bold")
        ax.set_xlabel("Output (Real GDP)")
        ax.set_ylabel("Price Level")
        ax.set_xlim(20, 90)
        ax.set_ylim(0, 7)
        ax.legend(fontsize=8)

    elif graph_type == "as_curves":
        # SRAS: P = 0.05*Y (passes through origin); LRAS vertical at Y* = 60.
        y_star = 60
        x_sras = np.linspace(20, 100, 100)
        y_sras = 0.05 * x_sras
        ax.plot(x_sras, y_sras, color=GOLD, linewidth=3, label="SRAS (short run)")
        ax.axvline(y_star, color=TEAL, linewidth=3, label="LRAS (long run)")
        p_meet = 0.05 * y_star
        ax.plot(y_star, p_meet, "o", color=CORAL, markersize=7, zorder=5)
        ax.annotate("Y*  (natural output)", (y_star, p_meet), textcoords="offset points",
                    xytext=(8, -14), color=MUTED, fontsize=8)
        ax.set_title("Short-Run vs Long-Run Aggregate Supply", fontsize=12, fontweight="bold")
        ax.set_xlabel("Output (Real GDP)")
        ax.set_ylabel("Price Level")
        ax.set_xlim(20, 100)
        ax.set_ylim(0, 6)
        ax.legend(fontsize=8)

    elif graph_type == "demand_shock":
        # All three curves are straight lines so the equilibrium markers are exact
        # algebraic intersections, not eyeballed points.
        y_star = 60
        x_sras = np.linspace(20, 100, 100)
        y_sras = 0.05 * x_sras                      # SRAS: P = 0.05*Y
        ax.plot(x_sras, y_sras, color=MUTED, linewidth=2.5, label="SRAS")
        ax.axvline(y_star, color=VIOLET, linewidth=2.2, label="LRAS")

        c1, c2, d = 8.4, 9.4, 0.09                  # AD:  P = c - d*Y
        y_ad = np.linspace(20, 93, 100)
        ax.plot(y_ad, c1 - d * y_ad, color=TEAL, linewidth=2.5, label="AD (before)")
        y_ad2 = np.linspace(20, 100, 100)
        ax.plot(y_ad2, c2 - d * y_ad2, color=GOLD, linewidth=2.5, linestyle="--", label="AD' (after shock)")

        # E0: SRAS ∩ AD   -> 0.05Y = c1 - dY
        y0 = c1 / (0.05 + d)
        p0 = 0.05 * y0
        # E1: SRAS ∩ AD'  -> 0.05Y = c2 - dY
        y1 = c2 / (0.05 + d)
        p1 = 0.05 * y1

        ax.plot(y0, p0, "o", color=TEAL, markersize=7, zorder=5)
        ax.annotate(f"E0", (y0, p0), textcoords="offset points", xytext=(-16, 6), color=PAPER, fontsize=9)
        ax.plot(y1, p1, "o", color=CORAL, markersize=7, zorder=5)
        ax.annotate(f"E1", (y1, p1), textcoords="offset points", xytext=(6, 6), color=PAPER, fontsize=9)

        ax.set_title("A Positive Demand Shock (short run)", fontsize=12, fontweight="bold")
        ax.set_xlabel("Output (Real GDP)")
        ax.set_ylabel("Price Level")
        ax.set_xlim(20, 100)
        ax.set_ylim(0, 6)
        ax.legend(fontsize=7.5, loc="upper left")

    style_axes(ax, fig)
    st.markdown('<div class="graph-frame">', unsafe_allow_html=True)
    st.pyplot(fig, width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 6. MASTERY TRACKER (session-based gamification)
# ==========================================
if "mastered" not in st.session_state:
    st.session_state.mastered = set()


def all_topics():
    for course, chapters in database.items():
        for chapter, topics in chapters.items():
            for topic in topics:
                yield (course, chapter, topic)


TOTAL_TOPICS = len(list(all_topics()))


# ==========================================
# 7. SIDEBAR - "COURSE LEDGER"
# ==========================================
st.sidebar.markdown('<div class="ledger-title">📚 Course Ledger</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="ledger-sub">University of Dhaka · Economics</div>', unsafe_allow_html=True)

courses = list(database.keys())
selected_course = st.sidebar.selectbox("1. Course", courses)

progress_pct = 0
if database[selected_course]:
    chapters = list(database[selected_course].keys())
    selected_chapter = st.sidebar.selectbox("2. Chapter", chapters)

    topics = list(database[selected_course][selected_chapter].keys())
    selected_topic = st.sidebar.selectbox("3. Topic", topics)
else:
    selected_chapter, selected_topic = None, None

mastered_count = len(st.session_state.mastered)
progress_pct = int(100 * mastered_count / TOTAL_TOPICS) if TOTAL_TOPICS else 0

st.sidebar.markdown(
    f"""
    <div class="progress-wrap">
        <div class="progress-label">Course Mastery</div>
        <div class="progress-track"><div class="progress-fill" style="width:{progress_pct}%;"></div></div>
        <div class="progress-count">{mastered_count} / {TOTAL_TOPICS} topics mastered</div>
    </div>
    <div class="study-tip">💡 Tip: a short 5–10 minute break every 45–50 minutes usually helps you remember more than pushing straight through.</div>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# 8. MAIN CONTENT - "TOPIC DOSSIER"
# ==========================================
if selected_topic:
    key = (selected_course, selected_chapter, selected_topic)
    content = database[selected_course][selected_chapter][selected_topic]

    st.markdown(f'<div class="breadcrumb">{selected_course} › {selected_chapter}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="topic-title">{selected_topic.replace("Topic: ", "").replace("Topic ", "")}</div>', unsafe_allow_html=True)

    is_mastered = key in st.session_state.mastered
    mastered_now = st.checkbox("✅ I've mastered this topic", value=is_mastered, key=f"chk_{key}")
    if mastered_now and not is_mastered:
        st.session_state.mastered.add(key)
        st.rerun()
    elif not mastered_now and is_mastered:
        st.session_state.mastered.discard(key)
        st.rerun()

    eq_divider()

    if content["graph"] != "none":
        draw_graph(content["graph"])

    render_explanation(content["explanation"])

    eq_divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'<div class="pyq-card"><div class="section-label" style="color:{CORAL};">📝 Previous Year Questions</div>{content["pyq"]}</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'<div class="ex-card"><div class="section-label" style="color:{VIOLET};">💪 Book Exercises</div>{content["exercise"]}</div>',
            unsafe_allow_html=True,
        )

else:
    st.markdown(f'<div class="breadcrumb">{selected_course}</div>', unsafe_allow_html=True)
    st.markdown('<div class="topic-title">Notes coming soon</div>', unsafe_allow_html=True)
    st.info("This course is on the ledger but the notes haven't been written yet. Keep up the great studying — add content here next.")
