import turtle
def lets_make_it_Awesome():
        """drawing fractels of square"""
	#opening screen
	window = turtle.Screen()

	# changing the background color
	window.bgcolor('green')


	# idenfing the brad turtle
	brad = turtle.Turtle()

	# reset some prop.s
	brad.shape('turtle')
	brad.color('black',"green")
	brad.speed('fast')
	brad.pensize(1)
	#making bigest triangle(container)
	
	sides_number = 2
	side_counts = 0

	while side_counts <= sides_number:
		brad.backward(375)
		brad.right(120)
		side_counts+=1

	brad.backward(375/2.)
	brad.right(120)
	brad.backward(375/2.)
	

	#making biger triangle

	sides_number = 2
	side_counts = 0

	while side_counts < sides_number:
		
		brad.right(60+180)
		brad.backward(375/2.)
		side_counts+=1
	
	brad.right(120)
	brad.backward(375/4.)


	brad.right(120)
	brad.backward(375/4.)
	sides_number = 2
	side_counts = 0
	while side_counts < sides_number:
		
		brad.right(60+180)
		brad.backward(375/4.)
		side_counts+=1

	brad.right(120)
	brad.forward(375/2.)
	brad.right(60+180)
	brad.forward(375/4.)

	sides_number = 2
	side_counts = 0
	while side_counts < sides_number:
		
		brad.right(120)
		brad.forward(375/4.)
		side_counts+=1
	brad.right(60+180)
	brad.forward(375/4.)
	brad.right(60+180)
	brad.forward(375/2. + 375/4.)	


	brad.right(120+180)
	brad.forward(375/4.)	

	sides_number = 2
	side_counts = 0
	while side_counts < sides_number:
		
		brad.right(60+180)
		brad.forward(375/4.)
		side_counts+=1

	brad.right(120+180)
	brad.forward(375/8.)	

	brad.right(120+180)
	brad.forward(375/8.)	
	sides_number = 2
	side_counts = 0
	while side_counts < sides_number:
		
		brad.right(60+180)
		brad.forward(375/8.)
		side_counts+=1
	i=0
	while i <=2 :	
		brad.right(120)
		brad.forward(375/4.)

		brad.right(120)
		brad.forward(375/8.)
		sides_number = 2
		side_counts = 0
		while side_counts < sides_number:
			
			brad.right(60+180)
			brad.forward(375/8.)
			side_counts+=1
		i+=1
	brad.right(120)
	brad.forward(375/8.)
	brad.right(120)
	brad.forward(375/4. + 375/8. )
	i = 0
	while i <= 2:
		
		brad.right(60)
		brad.forward( 375/8. )

		sides_number = 2
		side_counts = 0
		while side_counts < sides_number:
				
			brad.right(120)
			brad.forward(375/8.)
			side_counts+=1
		
		brad.right(60)
		brad.forward(375/4.)
		i+=1
	brad.color('green',"green")
	brad.backward(375/8.)
	brad.right(360-60)
	brad.color('black',"green")



	brad.backward(375 - (375/8) )
	i=0
	while i < 2 :	
		
		brad.forward(375/4.)
		brad.right(120 +180)
		brad.forward(375/8.)
		sides_number = 2
		side_counts = 0

		while side_counts < sides_number:
			
			brad.right(60+180)
			brad.forward(375/8.)
			side_counts+=1
		i+=1
		brad.right(120 +180)
		brad.backward(375/4.)
		brad.forward(375/4.)
	#closing the screen by clicking on it
	window.exitonclick()
lets_make_it_Awesome()
