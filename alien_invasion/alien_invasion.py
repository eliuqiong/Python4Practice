import sys
from time import sleep
from typing import Any

import pygame

from game_settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """define the resource of the game"""

    def __init__(self):
        """initial setting of the game"""
        pygame.init()
        self.settings = Settings()

	    # set the initial screen to full screen and then get the width and height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Game of 2023: Alien Invasion. Co-Authors: PAN & LIU")

        # create instances for game statistics, ship, bullet, aliens, button
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()
        # create a button to let user choose whether to play
        self.play_button = Button(self, "Play")
        self.scoreboard = Scoreboard(self)
    
    
    def run_game(self):
        """start the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                # monitor the mourse and keyboard events, update screen
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            

    def _check_events(self):
        """check and respond to mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """start a new game when click play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset the game status
            self.stats.reset_stats()
            self.stats.game_active = True
            self.settings.initialize_dynamic_settings()
            self.scoreboard.prep_score()
            self.scoreboard.prep_game_level()
            self.scoreboard.prep_ships_left()

            # get rid of aliens and ship
            self.aliens.empty()
            self.bullets.empty()

            # create new alien fleet and a ship
            self._create_alien_fleet()
            self.ship.center_ship()

            #hide mouse cursor
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self,event):
        """respons to key press down"""
        if event.key == pygame.K_RIGHT:
            # set the moving status to True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # set the moving status and stop to move
           self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            with open("highest_score_ever.txt","w") as highest_score:
                highest_score.write(str(self.stats.highest_score))
                highest_score.close()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """respons to key press up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
           self.ship.moving_left = False


    def _fire_bullet(self):
        """create a bullet and add it to the bullets Group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """update new bullets and remove old bullets"""
        #update bullets postions
        self.bullets.update()

        #remove bullets that fly beyond the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # want to check whether the bullets will disappear, print its number
            # print(len(self.bullets))

        self._check_bullet_alien_collision()
    

    def _check_bullet_alien_collision(self):
        # check for any bullets that hit alien, then get rid of that alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.scoreboard.update_highest_score()          
            self.scoreboard.prep_score()
        # if no alien left, then clear bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_speed()
            self.scoreboard.prep_highest_score()  
            #increase game level by 1
            self.stats.game_level += 1
            self.scoreboard.prep_game_level()

    def _create_alien_fleet(self):
        """create the alien fleet"""
        # start an alien
        alien = Alien(self)
        # number of aliens in one row, each alien take twice space as its own width
        alien_space_width = 4 * alien.rect.width
        available_space_x = self.settings.screen_width - alien_space_width
        number_aliens_x = available_space_x // alien_space_width
        # number of rows of aliens, leave space for two rows on top of the ship and one row on the top of the aliens
        available_space_y = self.settings.screen_height - (10 * alien.rect.height) - self.ship.rect.height
        number_aliens_row = available_space_y // ( 2 * alien.rect.height )

        # create the full fleet of alens
        for row_number in range(number_aliens_row):
            # create the first row of alens
            for alien_number in range(number_aliens_x):
                # create an alien and place it into the row
                self._create_alien(alien_number, row_number)
        

    def _create_alien(self, alien_number, row_number):
        """create one alien and place in a row"""
        alien = Alien(self)
        alien_space_width = 2 * alien.rect.width
        alien.x += alien_number * alien_space_width
        alien.rect.x = alien.x
        alien.rect.y += 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_aliens(self):
        """update the positions of alien fleet, moving to right side"""
        self._check_fleet_edges()
        self.aliens.update()            

        # tell the player that his ship was hit by the alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #print("MAYDAY! MAYDAY! SHIP HIT DOWN!")
            self._ship_hit()

        # if a alien arrive at the bottom, reset the game the same way as the ship was hit by an alien
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """cehck whether an alien survived and arrived at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # reset the game the same way as the ship was hit by an alien
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """if any alien reached edge, change direction accordingly"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_directions()
                break
    

    def _change_fleet_directions(self):
        """drop the entire fleet and change moving direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # reset fleet direction to move left, which means it is -1
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        """respond when ship was hit by an alien"""
        #decrease the ship numbers and when no ship left set the game status to de-active
        if self.stats.ships_left > 0:
            #decrease the ship number can be used
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships_left()

            # clear the screen
            self.aliens.empty()
            self.bullets.empty

            # start new game by create new fleet and a new ship
            self._create_alien_fleet()
            self.ship.center_ship()

            # pause for 0.5 seconds so that player can notice the update
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # draw the score info
        self.scoreboard.show_score()

        # pop up a button when the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_buttom()
        
        # display the most recent screen settings
        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance and run the game
    new_game = AlienInvasion()
    new_game.run_game()
