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
            "Topic: Production Possibilities": {
                "graph": "isoquant",
                "explanation": "📌 **THE CATCH:** Technology limits what a factory can do. An isoquant is a curve showing all the different ways to make the exact same amount of product.\n\n📖 **ELABORATION:** A production possibilities set describes all the realistic combinations of inputs and outputs a business can use. If a factory wants to make exactly one specific amount of goods, it can mix its inputs in different ways. For example, it might use more machines and fewer workers, or more workers and fewer machines. The curve that shows these equal-output combinations is called an isoquant. The slope of this curve is called the Technical Rate of Substitution. It tells us exactly how much of one input the factory has to give up to use a little more of another input, all while keeping the final output perfectly constant.",
                "pyq": "Define the Technical Rate of Substitution and explain its geometric meaning.",
                "exercise": "Review the difference between Cobb-Douglas and Leontief technology."
            },
            "Topic: Returns to Scale": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** Returns to scale tells us what happens to our output when we multiply all our inputs by the same amount.\n\n📖 **ELABORATION:** If doubling all your factory inputs gives you exactly double the output, that is called constant returns to scale. If output increases more than the scale of your inputs, it is called increasing returns to scale. If the output increases less than your inputs, it is decreasing returns to scale. This helps a business understand if it is a good idea to grow larger.",
                "pyq": "Explain the difference between increasing and decreasing returns to scale.",
                "exercise": "Calculate returns to scale for the CES production function."
            }
        },
        "Chapter 2: Profit Maximization": {
             "Topic: Maximizing Profits": {
                "graph": "profit_max",
                "explanation": "📌 **THE CATCH:** To make the highest profit, the money earned from making one extra item must exactly equal the cost of making it.\n\n📖 **ELABORATION:** Economic profit is the money a business keeps after paying for all its costs. A competitive firm cannot change market prices, so it only decides how much to produce. To find the maximum profit, we use an 'isoprofit line'. This line shows all the combinations of inputs and outputs that give the exact same profit amount. The firm wants to push this line as high as possible. On a graph, the absolute maximum profit happens exactly where the curve of the production function touches the isoprofit line. At this specific point, their slopes are perfectly equal.",
                "pyq": "Explain why a profit-maximizing firm will choose an input level where the isoprofit line is tangent to the production function.",
                "exercise": "Calculate the profit function for a simple Cobb-Douglas technology."
             }
        },
        "Chapter 7: Utility Maximization": {
             "Topic: Getting the Most Happiness": {
                "graph": "none",
                "explanation": "📌 **THE CATCH:** People have a limited budget and shop to find the bundle of goods that brings them the highest possible satisfaction.\n\n📖 **ELABORATION:** Consumers want to maximize their utility, which is just a fancy word for satisfaction or happiness. Because they have a fixed amount of money, they cannot buy everything. The expenditure function is a tool that tells us the absolute minimum amount of money a person needs to reach a specific level of happiness at current prices. Roy's Identity and Shephard's Lemma are mathematical shortcuts that let us instantly find a consumer's demand for a good just by looking at these utility and expenditure formulas.",
                "pyq": "State and prove Roy's identity and explain its usefulness.",
                "exercise": "Find the expenditure function for the Cobb-Douglas utility function."
             }
        },
        "Chapter 8: Choice": {
             "Topic: The Slutsky Equation": {
                "graph": "slutsky",
                "explanation": "📌 **THE CATCH:** When a price drops, you buy more for two reasons: the item is now a better deal than others, and your leftover money acts like a bonus paycheck.\n\n📖 **ELABORATION:** The Slutsky equation is a mathematical formula that splits a person's reaction to a price change into two separate pieces. The first piece is the Substitution Effect. If apples become cheaper than oranges, you naturally swap oranges for apples. The second piece is the Income Effect. Because apples are cheaper, you have more money left in your pocket after buying them. This extra purchasing power feels like getting a raise, so you use it to buy even more goods. The total change in your shopping cart is just the sum of these two effects.",
                "pyq": "Use the Slutsky equation to decompose a price change into substitution and income effects.",
                "exercise": "Draw the Hicks and Slutsky compensation bounds for a price increase."
             }
        }
    },
    "Advanced Macroeconomics": {},
    "Research Methodology": {},
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

# Check if the course has chapters
if database[selected_course]:
    chapters = list(database[selected_course].keys())
    selected_chapter = st.sidebar.selectbox("2. Choose a Chapter", chapters)
    
    topics = list(database[selected_course][selected_chapter].keys())
    selected_topic = st.sidebar.selectbox("3. Choose a Topic", topics)
    
    # Get the data for the chosen topic
    content = database[selected_course][selected_chapter][selected_topic]
    
    st.header(selected_topic)
    st.markdown("---")
    
    # Draw the graph if one exists for this topic
    if content["graph"] != "none":
        draw_graph(content["graph"])
        
    # Display the explanation text
    st.markdown(content["explanation"])
    
    st.markdown("---")
    st.subheader("📝 Previous Year Questions")
    st.info(content["pyq"])
    
    st.subheader("💪 Book Exercises")
    st.success(content["exercise"])
    
else:
    st.warning("Notes for this course are coming soon! Keep up the great studying.")
