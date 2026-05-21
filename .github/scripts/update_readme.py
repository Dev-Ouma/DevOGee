import random
import re
from pathlib import Path

QUOTES = [
    ("The question of whether a computer can think is no more interesting than the question of whether a submarine can swim.", "Edsger W. Dijkstra"),
    ("Programs must be written for people to read, and only incidentally for machines to execute.", "Harold Abelson"),
    ("Mathematics is not about numbers, equations, computations, or algorithms: it is about understanding.", "William Paul Thurston"),
    ("In mathematics you don't understand things. You just get used to them.", "John von Neumann"),
    ("Pure mathematics is, in its way, the poetry of logical ideas.", "Albert Einstein"),
    ("A mathematician, like a painter or a poet, is a maker of patterns.", "G. H. Hardy"),
    ("Computer science is no more about computers than astronomy is about telescopes.", "Edsger W. Dijkstra"),
    ("We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.", "Donald Knuth"),
    ("An algorithm must be seen to be believed.", "Donald Knuth"),
    ("A ship in port is safe, but that's not what ships are for.", "Grace Hopper"),
    ("The art of doing mathematics consists in finding that special case which contains all the germs of generality.", "David Hilbert"),
    ("The function of good software is to make the complex appear simple.", "Grady Booch"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("Without mathematics, there's nothing you can do. Everything around you is mathematics.", "Shakuntala Devi"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("The only way to learn a new programming language is by writing programs in it.", "Dennis Ritchie"),
    ("Data is the new oil, and the ability to refine it is the new engineering.", "Anonymous"),
    ("To understand recursion, one must first understand recursion.", "Anonymous"),
    ("Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "Bill Gates"),
    ("The advance of technology is based on making it fit in so that you don't really even notice it.", "Bill Gates"),
    ("Intelligence is the ability to adapt to change.", "Stephen Hawking"),
    ("Any sufficiently advanced technology is indistinguishable from magic.", "Arthur C. Clarke"),
    ("The most disastrous thing that you can ever learn is your first programming language.", "Alan Kay"),
    ("It is not enough to be in the right place at the right time. You should also have an open mind at the right time.", "Paul Erdős"),
    ("A good proof is one that makes us wiser.", "Yuri Manin"),
    ("God made the integers, all else is the work of man.", "Leopold Kronecker"),
    ("The difference between a good teacher and a great teacher is that a great teacher can reach anyone.", "Anonymous"),
    ("Education is not the filling of a pail, but the lighting of a fire.", "W.B. Yeats"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Technology is best when it brings people together.", "Matt Mullenweg"),
    ("Open source is not about being anti-commercial. It's about being pro-community.", "Anonymous"),
    ("Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime.", "Maimonides"),
    ("The beautiful thing about learning is that no one can take it away from you.", "B.B. King"),
    ("Real programmers count from 0.", "Anonymous"),
    ("There are only 10 types of people in the world: those who understand binary, and those who don't.", "Anonymous"),
    ("Weeks of coding can save you hours of planning.", "Anonymous"),
    ("Debugging is twice as hard as writing the code in the first place.", "Brian Kernighan"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
]


def update_readme():
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")

    quote_text, author = random.choice(QUOTES)
    new_quote = f'> *"{quote_text}"*\n>\n> — **{author}**'

    pattern = r"(<!-- QUOTE_START -->).*?(<!-- QUOTE_END -->)"
    replacement = f"\\1\n{new_quote}\n\\2"

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content != content:
        readme_path.write_text(new_content, encoding="utf-8")
        print(f'✅ Updated quote: "{quote_text[:70]}..." — {author}')
    else:
        print("⚠️  No <!-- QUOTE_START --> markers found in README.md")


if __name__ == "__main__":
    update_readme()
