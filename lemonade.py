import pygame
from pygame.locals import*


def game_init():
	img = pygame.image.load('lemon.jpg')

	white = (255, 64, 64)
	w = 640
	h = 480
	screen = pygame.display.set_mode((w, h))
	screen.fill((white))
	running = 1

	while running:
	    screen.fill((white))
	    screen.blit(img,(0,0))
	    pygame.display.flip()

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")

def daily_position():
	pass
	
def game():
	pygame.init()
	screen = pygame.display.set_mode((400, 300))
	done = False

	while not done:
	        for event in pygame.event.get():
	                if event.type == pygame.QUIT:
	                        done = True
	        
	        pygame.display.flip()


capital=200
monthly_interest=0.01

from random import randint

def get_random():
		dailycap_buyer=randint(9,27)/9
		lemon_price_var=randint(49,70)/70
		return dailycap_buyer,lemon_price_var

def round(item):
	if type(item) == int:
		return item
	else:
		if type(item) == float:
			pass
		else:
			if type(item) == str:
				try:
					item = float(int(item))
					round(item)
				except:
					try:
						item = float(item)
						round(item)
					except:
						raise ValueError("Must be a number")
	if item > float(int(item))+0.5:
		return int(item)+1
	return int(item)

def main(days,price,cost,buyer_min,initial_lemons, r=round):
	#game_init()
	total_rev=0
	nextday_lemons=initial_lemons
	for day in range(0,days):
		(buyer_var, price_var)=(randint(9,27)/9,randint(49,70)/70)
	  	if day==0:
	  		if buyer_min*buyer_var<=initial_lemons:
	  			nextday_lemons=nextday_lemons-1
	  			revenue=buyer_min*buyer_var*price-(initial_lemons*cost)
			else:
	  			revenue=initial_lemons*(price-cost)
				nextday_lemons=nextday_lemons+1
	  	else:
	  		lemon_i_have+=initial_lemons
	  		if buyer_min*buyer_var<=nextday_lemons:
				nextday_lemons=nextday_lemons-1
				print("wasted lemon"+str(nextday_lemons-buyer_min*buyer_var ))
	  			revenue=buyer_min*buyer_var*price-nextday_lemons*cost
	  		else:
				revenue=nextday_lemons*(price-cost)
				nextday_lemons=nextday_lemons+1
	  	revenue=r(revenue)
	  	total_rev+=revenue
	  	print([buyer_var*buyer_min*price, nextday_lemons,nextday_lemons*cost])
	  				
	  	print("day"+str(day)+" revenue is" + str(revenue)),

	  #screen = pygame.display.set_mode((320,240))
	  #print (ask(screen, "Name") + " was entered")

main(30,2,1,10,10)
