import time, os
love = ["________00000000000___________000000000000_________",
"______00000000_____00000___000000_____0000000______",
"____0000000_____________000______________00000_____",
"___0000000_______________0_________________0000____",
"__000000____________________________________0000___",
"__00000_____________________________________ 0000__",
"_00000______________________________________00000__",
"_00000_____________________________________000000__",
"__000000_________________________________0000000___",
"___0000000____________YÊU EM____________0000000____",
"_____000000____________________________000000______",
"_______000000________________________000000________",
"__________00000_____________________0000___________",
"_____________0000_________________0000_____________",
"_______________0000_____________000________________",
"_________________000_________000___________________",
"_________________ __000_____00_____________________",
"______________________00__00_______________________",
"________________________00_________________________",
""]

word = " Tình yêu là một thứ kỳ diệu. Nó kích thích và truyền cảm hứng. Nó khiến người ta đau khổ nhưng rất đỗi ngọt ngào. Tình yêu là khi anh và em cùng nhau chung sống. Chúc một mùa Valentine hạnh phúc sẽ đến với hai ta."

os.system("cls")
for i in love:
	print(i, flush=True)
	time.sleep(0.1)

for i in word:
	print(i, flush=True, end="")
	time.sleep(0.1)

input()
