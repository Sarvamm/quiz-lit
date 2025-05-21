import streamlit as st
import plotly.express as px
from streamlit_extras.buy_me_a_coffee import button
import streamlit.components.v1 as components

version: str = "0.0.1"
logo_gif: str = (
    "https://media1.tenor.com/m/d54XfQ2BGwcAAAAd/raccoon-circle-dance-round.gif"
)
coffee_username: str = "astrayn"

if "current_question_idx" not in st.session_state:
    st.session_state.current_question_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempted_questions" not in st.session_state:
    st.session_state.attempted_questions = set()
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 1
    
def load_questions():
    return  [
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na = [1,2,3]\na.append(a)\nprint(a[3][3][3][3][3])\n```",
        "image_link": "",
        "options": {
            "[1,2,3]": False,
            "[1,2,3, [1,2,3, [1,2,3] ]]": False,
            "[1, 2, 3, [...]]": True,
            "SyntaxError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = 11\nprint( [1,2,3,4] [( (x>=5) * 3 ) -2] )\n```",
        "image_link": "",
        "options": {
            "1": False,
            "2": True,
            "3": False,
            "4": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nseries = True, False, True, False\nif series:\n    print(series[False])\n```",
        "image_link": "",
        "options": {
            "False": False,
            "True, False, True, False": False,
            "None": False,
            "True": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint(1 << 1 ,'|',  1 >> 1)\n```",
        "image_link": "",
        "options": {
            "1 | 0": False,
            "2 | 1": False,
            "2 | 0": True,
            "1 | 1": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = (2 == 1) , (2 != 1) \nprint(x)\n```",
        "image_link": "",
        "options": {
            "(False, True)": True,
            "(True, False)": False,
            "(False, False)": False,
            "(True, True)": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na, *_ , b = ( bool(print) , bool(bool), bool(id('_')), bool(0), bool(int) )\n\nprint(_)\n```",
        "image_link": "",
        "options": {
            "[True, False, True]": False,
            "[False, True, True]": False,
            "[True, True, False]": True,
            "[True, False, False]": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = {1, 2}\ny = {2, 1}\n\nprint( (x | y) - x - y)\n```",
        "image_link": "",
        "options": {
            "{}": False,
            "set()": True,
            "None": False,
            "{{}}": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ndef operate( a:int, b:str, c:bool ) -> str | None:\n    return None if not c else a*b\n\noperate( **{'c':True, 'b':'False', 'a':2 } )\n```",
        "image_link": "",
        "options": {
            "'FalseFalse'": True,
            "None": False,
            "False": False,
            "NoneType": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nfns = square, double, triple, cube\n\na, *b, c = fns\n\nprint( b[0](b[-1](2)) )\n```",
        "image_link": "",
        "options": {
            "6": False,
            "8": False,
            "12": True,
            "24": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( \n    (x := 10) << 1 | 0 | 1\n      )\n```",
        "image_link": "",
        "options": {
            "12": False,
            "20": False,
            "5": False,
            "21": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( 1 ^ 2 ^ 3)\n```",
        "image_link": "",
        "options": {
            "1": False,
            "0": True,
            "6": False,
            "8": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( int( True | False and True or False | True ) + int(1e4))\n```",
        "image_link": "",
        "options": {
            "10000": False,
            "10001": True,
            "1e5": False,
            "1e4": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( type( id(1e9 / 1e4 ) ) )\n```",
        "image_link": "",
        "options": {
            "<class 'int'>": True,
            "<class 'float'>": False,
            "<class 'str'>": False,
            "<class 'bool'>": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( 10_00e2 - ( [1e2, 1e4][x := (True if 1e2 > 1e4 else False)] ))\n```",
        "image_link": "",
        "options": {
            "100.0": False,
            "9990.0": False,
            "990.0": False,
            "99900.0": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ny = set(( x := str(bool(str(None))) ).split() + x.split())\n\nprint(y)\n```",
        "image_link": "",
        "options": {
            "{'False'}": False,
            "{'True', 'True'}": False,
            "{'True'}": True,
            "set()": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( (None if any( [None, None, None]) else 0)  ==  (None if all( [None, None, None]) else 0)  )\n```",
        "image_link": "",
        "options": {
            "False": False,
            "None": False,
            "NoneType": False,
            "True": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nnot all(\n    list(\n        map(\n            eval,\n            (\n                (str(None) + \" \")* int(1e5))\n            .split()\n            )\n        )\n    ) and bool(False)\n```",
        "image_link": "",
        "options": {
            "0": False,
            "True": False,
            "None": False,
            "False": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nfn = lambda x: 1 if x == 1 else fn(x-1)  \n\nprint( fn(4) << fn(1) )\n```",
        "image_link": "",
        "options": {
            "False": False,
            "True": False,
            "2": True,
            "infinite loop": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ntry:\n    print(print)\nexcept:\n    print( x:= all( (True or False, True and False) ) )\nfinally:\n    print( x )\n```",
        "image_link": "",
        "options": {
            "<built-in function print>\nTrue": True,
            "SyntaxError": False,
            "True\nTrue": False,
            "<built-in function print>\n<built-in function print>\n": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nclass foo:\n    pass\nclass bar:\n    pass\n\nprint( id(foo) == id(bar) )\n```",
        "image_link": "",
        "options": {
            "0": False,
            "False": True,
            "True": False,
            "SyntaxError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nsquare = lambda x: x**2\ndouble = lambda x: x*2\n\nx, y = square(2), double(2)\n\nprint( [square(3), double(3)][id(x) == id(y)] )\n```",
        "image_link": "",
        "options": {
            "3": False,
            "9": False,
            "12": False,
            "6": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = 'Hi' 'This' 'is' 'a' 'hard' 'quiz'\ny = 'Hi', 'This', 'is', 'a', 'hard', 'quiz'\n\ntry:\n    print( x + y )\nexcept Exception:\n    print( type(x) == type(y)  )\n```",
        "image_link": "",
        "options": {
            "False": True,
            "True": False,
            "'HiThisisahardquizHiThisisahardquiz'": False,
            "TypeError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na = (x for x in 'a''b''c')\n\nprint(\n    next(a),\n    next(a),\n    next(a)\n    )\n```",
        "image_link": "",
        "options": {
            "a b c": True,
            "a, b, c": False,
            "(a, b, c)": False,
            "Error": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\n(lambda x: x-1 if isinstance(x, int) else x*(-1))('123')\n```",
        "image_link": "",
        "options": {
            "122": False,
            "''": True,
            "'321'": False,
            "Error": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint((() == ()) == ())\n```",
        "image_link": "",
        "options": {
            "True": False,
            "False": True,
            "TypeError": False,
            "SyntaxError": False
        }
    }
]
    

# Load questions
questions = load_questions()
st.session_state.total_questions = len(questions)
total_questions = st.session_state.total_questions

total_questions = st.session_state.total_questions
st.logo(logo_gif, size="large")


@st.dialog("Instructions")
def show_instructions():
    st.markdown("""
                This is a 4 option Multiple Choice Question (MCQ) quiz.
                There is no time limit, and you can take as much time as you need to answer each question.
                Select the correct answer from the options given. 
                You have to select one option before you can proceed to the next question.
                You cannot go back to the previous questions.
                Your score will be updated after each question.
                You can also check your score at the end of the quiz. Good luck!
                """)

@st.dialog("Share this quiz!")
def share_quiz():
    st.markdown("Share this quiz with others!")       
    link1 = "https://www.linkedin.com/feed/?shareActive&mini=true&text="
    link2 = f"I just scored {st.session_state.score}/23 in this awesome %20%23Python quiz created by @Sarvamm Rathore on  %20%23Streamlit ! Can you beat my score? Check it out here! https://pythonhardquiz.streamlit.app/"
    link = link1 + link2
    st.markdown(
    f'<a href="{link}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Linkedin</a>',
    unsafe_allow_html=True
)
        

@st.dialog(" ", width="large")
def about_creator():
    st.markdown(
        """
<style>
    .stApp {
        background-color: #00010f;
        color: #f0f0f0;
    }

    h1 {
        text-align: center;
        color: #f0f0f0;
        font-size: 2.5rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #a0a0a0;
        margin-bottom: 2rem;
    }


    .social-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(135deg, #1f1f1f, #292929);
    color: #00bfff;
    text-decoration: none;
    border-radius: 12px;
    margin: 0.5rem;
    width: 160px;
    border: 1px solid rgba(0, 191, 255, 0.2);
    box-shadow: 0 0 8px rgba(0, 191, 255, 0.2);
    transition: all 0.3s ease;
    font-weight: 500;
    }

    .social-btn img {
        filter: brightness(0) invert(1);
        transition: transform 0.3s ease;
    }

    .social-btn:hover {
        background: linear-gradient(135deg, #0f2027, #203a43);
        color: #ffffff;
        border-color: #00bfff;
        box-shadow: 0 0 12px rgba(0, 191, 255, 0.6);
        transform: translateY(-2px);
    }

    .social-btn:hover img {
        transform: scale(1.1);
    }


    .social-btn:hover {
        background-color: #2c3e50;
        transform: translateY(-3px);
    }

    .coffee-section {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #a0a0a0;
        font-size: 0.9rem;
    }

    #MainMenu, header {visibility: hidden;}
</style>
""",
        unsafe_allow_html=True,
    )

    # Profile circle
    st.markdown(
        f"""
    <div style="display: flex; justify-content: center; margin-top:-4rem;">
        <img src="https://media.licdn.com/dms/image/v2/D5603AQHt8xwJzuPRGQ/profile-displayphoto-shrink_400_400/B56ZQCcJF1H0Ag-/0/1735207720107?e=1753315200&v=beta&t=mr0xeQ0aDHu7Deg03o6UVG-zzl8PTvHE2cP6Ri9IqaE" alt="Profile" style="
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%;
            border: 3px solid #8e44ad;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        ">
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Title & subtitle
    st.markdown("<h1>Sarvamm</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Data Science Student | AI Enthusiast</p>',
        unsafe_allow_html=True,
    )

    # About Section
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown(
        """
    <p style="text-align: justify; text-align-last: center;">
    First year Data Science student specializing in AI and machine learning. Experienced in Python, SQL, and data visualization, with hands-on projects in predictive modeling and NLP. Constantly learning and exploring the field of intelligent systems. Open to discussions and collaboration!
    </p>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Social Links
    # Social Links with images
    st.markdown(
        """
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-top: 1rem;">
        <a href="https://linkedin.com/in/sarvamm" target="_blank" class="social-btn">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20" height="20">
            LinkedIn
        </a>
        <a href="https://github.com/Sarvamm" target="_blank" class="social-btn">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20" height="20">
            GitHub
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Buy Me a Coffee
    st.markdown(
        '<p style="text-align: center; margin-top: 2rem;">☕ If you like my work, support me here:</p>',
        unsafe_allow_html=True,
    )
    components.html(
        """
        <div style="display: flex; justify-content: center;">
            <a href="https://www.buymeacoffee.com/astrayn" target="_blank">
                <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
                    alt="Buy Me A Coffee" 
                    style="height: 60px !important; width: 217px !important;" >
            </a>
        </div>
    """,
        height=100,
    )


with st.sidebar:
    st.header("Progress")
    try:
        st.progress(len(st.session_state.attempted_questions) / total_questions)
    except ZeroDivisionError:
        st.progress(len(st.session_state.attempted_questions) / 1)
    st.write(
        f"Questions attempted: {len(st.session_state.attempted_questions)}/{total_questions}"
    )
    if st.button("Instructions"):
        show_instructions()
    if st.button("share this quiz!"):
        share_quiz()
    if st.button("About creator"):
        about_creator()
        
    st.markdown(8 * "<br>", unsafe_allow_html=True)
    st.caption("Support me by clicking on this button 👇")
    button(username=coffee_username, floating=False, width=221)
    st.caption(version)


# Main quiz interface
if not st.session_state.quiz_completed:
    if st.session_state.current_question_idx < total_questions:
        current_question = questions[st.session_state.current_question_idx]

        # Display question
        st.markdown(f"### {current_question['question']}")

        # Display extra content if available
        if current_question["extra_content"]:
            con = st.container(border=True)
            con.write(current_question["extra_content"])

        # Display image if available
        if current_question["image_link"]:
            st.markdown(
                f"""![Photo]({current_question["image_link"]})""",
                unsafe_allow_html=True,
            )

        # Create two columns for options
        col1, col2 = st.columns(2)

        # Get the options
        options = current_question["options"]
        option_items = list(options.keys())
        st.divider()
        # Display options in columns
        with col1:
            c1 = st.container(border=True)
            c2 = st.container(border=True)
            c1.markdown("A: " + option_items[0])
            c2.markdown("B: " + option_items[1])
        with col2:
            c1 = st.container(border=True)
            c2 = st.container(border=True)
            c1.markdown("C: " + option_items[2])
            c2.markdown("D: " + option_items[3])

        choice = st.radio("Select an option", ["A", "B", "C", "D"])

        if st.button("Next Question"):
            if choice:
                answer = (
                    option_items[0]
                    if choice == "A"
                    else option_items[1]
                    if choice == "B"
                    else option_items[2]
                    if choice == "C"
                    else option_items[3]
                    if choice == "D"
                    else None
                )
                if options[answer]:
                    st.session_state.score += 1
                    st.session_state.attempted_questions.add(
                        st.session_state.current_question_idx
                    )
                else:
                    st.session_state.attempted_questions.add(
                        st.session_state.current_question_idx
                    )
                st.session_state.current_question_idx += 1
            st.rerun()

    # Check if quiz is complete
    if st.session_state.current_question_idx >= total_questions:
        st.session_state.quiz_completed = True
        st.rerun()

# End screen
if st.session_state.quiz_completed:
    st.header("Quiz Complete!", divider=True)

    fig = px.pie(
        names=["Correct", "Incorrect"],
        values=[
            st.session_state.score,
            total_questions - st.session_state.score,
        ],
        hole=0.6,
        color_discrete_sequence=("#20ED5D", "#ED2071"),
        title=f"You scored {st.session_state.score} out of {total_questions} questions right!",
    )
    con = st.container(border=True)
    con.plotly_chart(fig)

    con2 = st.container(border=True)
    con2.markdown("Check out the card below for solutions!")
    con2.markdown(
        """ <a target="_blank" href="https://github-readme-medium-recent-article.vercel.app/medium/@srvmrtr/0"><img src="https://github-readme-medium-recent-article.vercel.app/medium/@srvmrtr/0" alt="Recent Article 0"> """,
        unsafe_allow_html=True,
    )
