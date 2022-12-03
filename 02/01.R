# AX rock, BY paper, CZ scissors
dt <- fread("02/input.txt", header = F, col.names = c("a", "b"))
val <- fread("
c;v
X;1
Y;2
Z;3
", key="c")

duel <- fread("
a;b;z
A;X;3
A;Y;6
A;Z;0
B;X;0
B;Y;3
B;Z;6
C;X;6
C;Y;0
C;Z;3
", key=c("a", "b")
)

strateg <- fread("
a;b;w
A;X;Z
B;X;X
C;X;Y
A;Y;X
B;Y;Y
C;Y;Z
A;Z;Y
B;Z;Z
C;Z;X
", key=c("a", "b"))


dt[, sc := val[dt$b, v]]
dt[, sd := duel[.(dt$a, dt$b), z]]
dt[, sum(sc+sd)]

dt[, c := strateg[.(dt$a, dt$b), w]]
dt[, tc := val[dt$c, v]]
dt[, td := duel[.(dt$a, dt$c), z]]
dt[, sum(tc+td)]
