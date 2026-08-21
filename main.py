import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. PAGE SETUP
# ==========================================
st.set_page_config(page_title="My Economics Study Hub", page_icon="📈", layout="wide")

# ==========================================
# 2. THE DATABASE (Your Digital Filing Cabinet)
# ==========================================
database = {
    "Advanced Microeconomics": {
        "Chapter 1: Technology": {
            "Topic: Production Possibilities & Isoquants": {
                "graph": "isoquant",
                "explanation": "📌 **THE CATCH:** A business takes inputs like labor and machines to create outputs. An isoquant is a curve showing all the different input recipes to make the exact same amount of output.\n\n📖 **ELABORATION:** A production possibilities set describes all the realistic combinations of inputs and outputs a business can technologically use[cite: 2]. The curve that shows equal-output combinations is called an isoquant[cite: 2]. The slope of this curve is called the Technical Rate of Substitution (TRS)[cite: 2]. It tells us exactly how much of one input the factory has to give up to use a little more of another input, all while keeping the final output perfectly constant[cite: 2].",
                "pyq": "Define the Technical Rate of Substitution and explain its geometric meaning.",
                "exercise": "Review the difference between Cobb-Douglas and Leontief technology."
            },
            "Topic: Returns to Scale": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** Returns to scale tells us what happens to our output when we multiply all our inputs by the same amount.\n\n📖 **ELABORATION:** If doubling all your factory inputs gives you exactly double the output, that is called constant returns to scale[cite: 2]. If output increases more than the scale of your inputs, it is called increasing returns to scale[cite: 2]. If the output increases less than your inputs, it is decreasing returns to scale[cite: 2]. The elasticity of scale measures the exact percentage increase in output caused by a one percent increase in all inputs[cite: 2].",
                "pyq": "Explain the difference between increasing and decreasing returns to scale.",
                "exercise": "Calculate returns to scale for the CES production function where rho = 1."
            }
        },
        "Chapter 2: Profit Maximization": {
             "Topic: Maximizing Profits": {
                "graph": "profit_max",
                "explanation": "📌 **THE CATCH:** To make the highest profit, the money earned from making one extra item must exactly equal the cost of making it.\n\n📖 **ELABORATION:** Economic profit is the revenue a business receives minus all the economic costs it incurs[cite: 3]. A competitive firm cannot change market prices, so it only decides how much to produce[cite: 3]. To find the maximum profit, we use an 'isoprofit line'. This line shows all the combinations of inputs and outputs that give the exact same profit amount[cite: 3]. On a graph, the absolute maximum profit happens exactly where the curve of the production function touches the isoprofit line[cite: 3].",
                "pyq": "Explain why a profit-maximizing firm will choose an input level where the isoprofit line is tangent to the production function.",
                "exercise": "Calculate the profit function for a simple Cobb-Douglas technology."
             }
        },
        "Chapter 7: Utility Maximization": {
             "Topic: Getting the Most Happiness": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** People have a limited budget and shop to find the bundle of goods that brings them the highest possible satisfaction.\n\n📖 **ELABORATION:** Consumers want to maximize their utility, which is just a fancy word for satisfaction. The expenditure function is a tool that tells us the absolute minimum amount of money a person needs to reach a specific level of happiness at current prices[cite: 3]. Roy's Identity and Shephard's Lemma are mathematical shortcuts that let us instantly find a consumer's demand for a good just by looking at these utility and expenditure formulas[cite: 3].",
                "pyq": "State and prove Roy's identity and explain its usefulness[cite: 2].",
                "exercise": "Find the expenditure function for the Cobb-Douglas utility function[cite: 3]."
             }
        },
        "Chapter 8: Choice": {
             "Topic: The Slutsky Equation": {
                "graph": "slutsky",
                "explanation": "📌 **THE CATCH:** When a price drops, you buy more for two reasons: the item is now a better deal than others, and your leftover money acts like a bonus paycheck.\n\n📖 **ELABORATION:** The Slutsky equation is a mathematical formula that splits a person's reaction to a price change into two separate pieces[cite: 3]. The first piece is the Substitution Effect: you naturally swap more expensive goods for the cheaper good[cite: 3]. The second piece is the Income Effect: because the good is cheaper, you have more purchasing power left over, which feels like getting a raise[cite: 3]. The total change in your demand is the sum of these two effects[cite: 3].",
                "pyq": "Use the Slutsky equation to decompose a price change into substitution and income effects.",
                "exercise": "Draw the Hicks and Slutsky compensation bounds for a price increase[cite: 3]."
             },
             "Topic: Revealed Preference": {
                 "graph": "none",
                 "explanation": "📌 **THE CATCH:** We can figure out what a person likes just by watching what they choose to buy in the store.\n\n📖 **ELABORATION:** Revealed preference analyzes observable variables to see if consumers are making rational choices[cite: 3]. The Generalized Axiom of Revealed Preference (GARP) states that if bundle A is revealed to be preferred to bundle B, bundle B cannot be strictly preferred to A[cite: 3]. If a person's shopping data is consistent with GARP, there exists a utility function that perfectly explains their behavior[cite: 3].",
                 "pyq": "No previous questions recorded yet.",
                 "exercise": "Review the differences between WARP, SARP, and GARP[cite: 3]."
             }
        }
    },
    "Advanced Macroeconomics": {
        "Chapter 10: Economic Fluctuations": {
            "Topic: Introduction": {
                "graph": "none",
                "explanation": "Type your notes from Mankiw 9th Edition here.",
                "pyq": "Add questions here.",
                "exercise": "Add exercises here."
            }
        }
    },
    "Research Methodology": {
        "Module 1: Foundations": {
            "Topic 1: Introduction to Research": {
                "graph": "none",
                "explanation": "Type your notes from Siratul Mustaquim here.",
                "pyq": "Add questions here.",
                "exercise": "Add exercises here."
            }
        }
    },
    "Environmental Economics": {},
    "Monetary Economics": {}
}

# ==========================================
# 3. THE GRAPHING ENGINE
# ==========================================
def draw_graph(graph_type):
    fig, ax = plt.subplots(figsize=(6, 4))
    
    if graph_type == "isoquant":
        x = np.linspace(0.5, 10, 100)
        y = 10 / x
        ax.plot(x, y, color='#1CB0F6', linewidth=3)
        ax.set_title('Isoquant Curve', fontsize=12, fontweight='bold')
        ax.set_xlabel('Factor 1', fontsize=10)
        ax.set_ylabel('Factor 2', fontsize=10)
        ax.grid(color='#E5E5E5', linestyle='--', linewidth=0.5)
        
    elif graph_type == "profit_max":
        x_prod = np.linspace(0, 10, 100)
        y_prod = np.sqrt(x_prod) * 3 
        x_profit = np.linspace(0, 10, 100)
        y_profit = 0.5 * x_profit + 2.25
        ax.plot(x_prod, y_prod, color='#CE82FF', linewidth=3, label='Production Curve')
        ax.plot(x_profit, y_profit, color='#58CC02', linewidth=2, linestyle='--', label='Isoprofit Line')
        ax.plot(4.5, np.sqrt(4.5)*3, 'ko', markersize=8) 
        ax.set_title('Profit Maximization Point', fontsize=12, fontweight='bold')
        ax.set_xlabel('Input Amount', fontsize=10)
        ax.set_ylabel('Output Amount', fontsize=10)
        ax.legend()
        
    elif graph_type == "slutsky":
        x_indiff = np.linspace(1, 10, 100)
        y_indiff1 = 12 / x_indiff
        y_indiff2 = 20 / x_indiff
        ax.plot(x_indiff, y_indiff1, color='#FF9600', linewidth=2, label='Old Utility')
        ax.plot(x_indiff, y_indiff2, color='#FF9600', linewidth=2, label='New Utility')
        ax.plot([0, 8], [8, 0], color='black', linewidth=1.5, label='Old Budget')
        ax.plot([0, 12], [8, 0], color='blue', linewidth=1.5, label='New Budget')
        ax.set_title('Substitution & Income Effects', fontsize=12, fontweight='bold')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.legend()

    st.pyplot(fig)

# ==========================================
# 4. THE USER INTERFACE (What you see)
# ==========================================
st.sidebar.title("📚 Study Menu")
courses = list(database.keys())
selected_course = st.sidebar.selectbox("1. Choose a Course", courses)

st.title(f"📖 {selected_course}")

if database[selected_course]:
    chapters = list(database[selected_course].keys())
    selected_chapter = st.sidebar.selectbox("2. Choose a Chapter", chapters)
    
    topics = list(database[selected_course][selected_chapter].keys())
    selected_topic = st.sidebar.selectbox("3. Choose a Topic", topics)
    
    content = database[selected_course][selected_chapter][selected_topic]
    
    st.header(selected_topic)
    st.markdown("---")
    
    if content["graph"] != "none":
        draw_graph(content["graph"])
        
    st.markdown(content["explanation"])
    
    st.markdown("---")
    st.subheader("📝 Previous Year Questions")
    st.info(content["pyq"])
    
    st.subheader("💪 Book Exercises")
    st.success(content["exercise"])
    
else:
    st.warning("Notes for this course are coming soon! Keep up the great studying.")
