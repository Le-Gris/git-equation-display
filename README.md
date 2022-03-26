# git-equation-display
A short script that parses files (i.e. README.md's) to change LaTex equations surrounded by '$' signs to links to equation images.

## Example

Say your `README.md` contains the following equation $\[ \lim_{n\to\infty} f(x) = 0 \]$ but you would like it to be displayed nicely. Then run `python3 make-equations.py README.md` and your document will now contain this equation instead: <img src="https://render.githubusercontent.com/render/math?math= \[ \lim_{n\to\infty} f(x) = 0 \]"> 
