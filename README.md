# 🎮 OpenGL Mini Games

This repository contains two interactive **OpenGL-based games** written in Python using **PyOpenGL** and **GLUT**.
They demonstrate computer graphics techniques such as the **Midpoint Circle Algorithm**, **Midpoint Line Algorithm**, real-time rendering, and interactive input handling.

---

## 🕹️ Games Included

### 1️⃣ Circle Shooter

A shooting game where:

* You control a circular shooter at the bottom of the screen.
* Move left and right to avoid collisions and shoot falling circles.
* Score points by hitting opponents.
* The game ends if you collide, miss too many bullets, or let too many enemies pass.

**Controls:**

* `A` → Move left
* `D` → Move right
* `Spacebar` → Shoot
* Mouse:

  * Left click **Pause/Resume**
  * Left click **Restart** (top-left icon)
  * Left click **Exit** (top-right icon)

---

### 2️⃣ Diamond Catcher

A reflex-based catching game where:

* A diamond falls from the top of the screen.
* You control a catcher at the bottom.
* Catch the diamond to score and increase difficulty (fall speed increases).
* The game ends if you miss a diamond.

**Controls:**

* `←` → Move left
* `→` → Move right
* Mouse:

  * Left click **Pause/Resume**
  * Left click **Restart** (top-left icon)
  * Left click **Exit** (top-right icon)

---

## ⚙️ Installation & Setup

### Requirements

Make sure you have **Python 3.x** installed along with:

* `PyOpenGL`
* `PyOpenGL_accelerate`
* `GLUT` (via `freeglut` or equivalent)

Install dependencies:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

On Linux (if GLUT is missing):

```bash
sudo apt-get install freeglut3-dev
```

### Running the Games

Clone this repository and run either game:

```bash
# Clone repo
git clone https://github.com/your-username/OpenGL-Games.git
cd OpenGL-Games

# Run Circle Shooter
python CircleShooter.py

# Run Diamond Catcher
python Diamondgame.py
```

---

## 📖 Learning Outcomes

Through these games you can learn:

* **Midpoint Line & Circle Drawing Algorithms**
* **Keyboard and Mouse Event Handling** in OpenGL
* **Animation using GLUT Idle Functions**
* Basics of **2D Game Development** in Python with OpenGL


---


## 📜 License

This project is licensed under the **MIT License**.

---

👨‍💻 **Author:** [Mehedi Hasan Shahed](https://github.com/MehediHasanShahed)
