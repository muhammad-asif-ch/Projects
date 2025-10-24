# 🎮 Tic Tac Toe using Minimax + Alpha-Beta Pruning (Python)

A simple yet intelligent **Tic Tac Toe** game implemented in **Python**, featuring an unbeatable **AI opponent** that uses the **Minimax algorithm** with **Alpha-Beta Pruning**.  
This version is optimized for **Jupyter Notebook** and includes smooth animations and clean board updates.

---

## 🧠 Features

- ✅ Play Tic Tac Toe against an AI powered by **Minimax + Alpha-Beta Pruning**  
- ✅ Interactive **CLI board** with clean display in Jupyter  
- ✅ **AI thinking animation** for realism  
- ✅ Detects **win**, **draw**, and **invalid moves**  
- ✅ Uses **game tree optimization** for faster AI decisions  

---

## 🖥️ Demo Screenshot

*(Example output in Jupyter Notebook)*

🎮 Tic Tac Toe using Minimax + Alpha-Beta Pruning (Jupyter Version)

 <!-- Sample Tic Tac Toe board with X and O (inline SVG) -->
<div align="center">

# Tic Tac Toe — Sample Game

<img alt="Tic Tac Toe - Sample" src="data:image/svg+xml;utf8,
%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20300'%20width='300'%20height='300'%3E
%3Crect%20width='100%25'%20height='100%25'%20fill='%23ffffff'/%3E
%3Cg%20stroke='%23000000'%20stroke-width='8'%20stroke-linecap='round'%3E
%3Cline%20x1='100'%20y1='10'%20x2='100'%20y2='290'/%3E
%3Cline%20x1='200'%20y1='10'%20x2='200'%20y2='290'/%3E
%3Cline%20x1='10'%20y1='100'%20x2='290'%20y2='100'/%3E
%3Cline%20x1='10'%20y1='200'%20x2='290'%20y2='200'/%3E
%3C/g%3E
%3Ctext%20x='50'%20y='95'%20font-size='80'%20text-anchor='middle'%20dominant-baseline='middle'%20font-family='Arial'%20fill='%23d32f2f'%3EX%3C/text%3E
%3Ctext%20x='150'%20y='155'%20font-size='80'%20text-anchor='middle'%20dominant-baseline='middle'%20font-family='Arial'%20fill='%23007bb8'%3EO%3C/text%3E
%3Ctext%20x='250'%20y='95'%20font-size='80'%20text-anchor='middle'%20dominant-baseline='middle'%20font-family='Arial'%20fill='%23d32f2f'%3EX%3C/text%3E
%3C/text%3E
%3C/svg%3E" />

</div>


Enter your move (1-9): - X

---

## ⚙️ How It Works

The game is based on the **Minimax algorithm**, a recursive decision-making process that explores all possible game outcomes to determine the optimal move.

### 🔹 Minimax Algorithm
- The **AI** assumes the opponent (you) will always play optimally.  
- It tries to **maximize its winning chances** and minimize yours.  
- The game state tree is explored recursively.

### 🔹 Alpha-Beta Pruning
- An optimization technique that **cuts off unnecessary branches** in the game tree.  
- Reduces computation time while maintaining the same results as standard Minimax.

---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://muhammad-asif-ch/Projects/tic-tac-toe-minimax.git
cd tic-tac-toe-minimax

### 2. Run the game in Jupyter Notebook
Open the `.ipynb` file or paste the code in a new Jupyter Notebook cell and run it:
jupyter notebook

### 3. Play the game
Enter numbers **1–9** to make your move according to this layout:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

---

## 🧩 Dependencies

- Python 3.7+
- Jupyter Notebook
- IPython (for clear_output animation)

To install required packages:
pip install notebook ipython

---

## 🏗️ Project Structure

tic_tac_toe_minimax.ipynb   # Main game (Jupyter Notebook)
README.txt                  # Project documentation
requirements.txt            # Dependencies (optional)

---

## 🧑‍💻 Author

**Muhammad Asif**  
🎓 BS Computer Science | 3rd Semester  
💡 Passionate about Python, AI, and Game Development  

---

## 📜 License

This project is open-source under the **MIT License**.  
Feel free to use, modify, and share it with proper credit.

---

## 🌟 Future Improvements

- Add a **GUI version** using `tkinter` or `pygame`  
- Add **score tracking** and **restart option**  
- Convert into a **Python script (.py)** for terminal play  
- Build a **web version** using Flask or React  

---

## 💬 Feedback

If you like this project or have suggestions for improvements, feel free to:
- ⭐ Star the repo  
- 🐞 Open an issue  
- 🛠️ Submit a pull request

---

> “An unbeatable AI is not magic — it’s math.”  
> — Muhammad Asif 🧠
