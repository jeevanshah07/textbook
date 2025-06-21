set table "new.pgf-plot.table"; set format "%.5f"
 f(x,y) = (x**3)+(y**3)-9*x*y; set xrange [-5.2:5.2]; set yrange [-5.2:5.2]; set view 0,0; set isosample 500,500; set cont base; set cntrparam levels incre 0,0.1,0; unset surface; splot f(x,y); 
