
import unittest, constants
from unittest.mock import *
from block import *
from game_screen import *
from title_screen import *
from art import *
from purse import *
from sound import *
from inventory import *
from rabbit import *

#Basic test to see if Block can be created
class test_Block(unittest.TestCase):

    @patch('block.pygame')
    def test_Block_can_be_created(self, mock_pygame):
        self.image = Mock()
        self.image.get_rect = Mock()
        block = Block(self.image, 50, 50)
        self.assertTrue(True)

#Test Carrots Here
class test_Carrot(unittest.TestCase):

    def setUp(self):
        self.carrot = Carrot(50, 50)
        self.time = 0

    def test_Carrot_can_be_created(self):
        self.assertTrue(True)

    @patch('carrot.pygame')
    def test_Carrot_changes_color_after_five_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=5001)
        self.carrot.image = Mock()
        self.carrot.art = Mock()
        self.carrot.art.get_image = Mock()
        self.carrot.grow()
        self.carrot.art.get_image.assert_called_with('carrot2')

    @patch('carrot.pygame')
    def test_Carrot_is_eatable_after_five_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=5001)
        self.carrot.grow()
        self.assertEqual(self.carrot.eatable, True)

    @patch('carrot.pygame')
    def test_Carrot_changes_color_after_ten_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=10001)
        self.carrot.image = Mock()
        self.carrot.art = Mock()
        self.carrot.art.get_image = Mock()
        self.carrot.grow()
        self.carrot.art.get_image.assert_called_with('carrot3')

    @patch('carrot.pygame')
    def test_Carrot_is_harvestable_after_ten_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=10001)
        self.carrot.grow()
        self.assertEqual(self.carrot.harvestable, True)

#Test Cabbages Here!
class test_Cabbage(unittest.TestCase):

    def setUp(self): 
        self.cabbage = Cabbage(50, 50)
        self.time = 0

    def test_Cabbage_can_be_created(self):
        self.assertTrue(True)

    @patch('cabbage.pygame')
    def test_Cabbage_changes_color_after_ten_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=10001)
        self.cabbage.image = Mock()
        self.cabbage.art = Mock()
        self.cabbage.art.get_image = Mock()
        self.cabbage.grow()
        self.cabbage.art.get_image.assert_called_with('cabbage2')

    @patch('cabbage.pygame')
    def test_Cabbage_is_eatable_after_ten_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=10001)
        self.cabbage.grow()
        self.assertEqual(self.cabbage.eatable, True)

    @patch('cabbage.pygame')
    def test_Cabbage_changes_color_after_twenty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=20001)
        self.cabbage.image = Mock()
        self.cabbage.art = Mock()
        self.cabbage.art.get_image = Mock()
        self.cabbage.grow()
        self.cabbage.art.get_image.assert_called_with('cabbage3')

    @patch('cabbage.pygame')
    def test_Cabbage_is_harvestable_after_twenty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=20001)
        self.cabbage.grow()
        self.assertEqual(self.cabbage.harvestable, True)

#Test Peppers Here!
class test_Pepper(unittest.TestCase):

    def setUp(self):
        self.pepper = Pepper(50, 50)
        self.time = 0
        self.color = constants.GREEN

    def test_Pepper_can_be_created(self):
        self.assertTrue(True)

    @patch('pepper.pygame')
    def test_Pepper_changes_color_after_fifteen_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=15001)
        self.pepper.image = Mock()
        self.pepper.art = Mock()
        self.pepper.art.get_image = Mock()
        self.pepper.grow()
        self.pepper.art.get_image.assert_called_with('pepper2')

    @patch('pepper.pygame')
    def test_Pepper_is_eatable_after_fifteen_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=15001)
        self.pepper.grow()
        self.assertEqual(self.pepper.eatable, True)

    @patch('pepper.pygame')
    def test_Pepper_changes_color_after_thirty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=30001)
        self.pepper.image = Mock()
        self.pepper.art = Mock()
        self.pepper.art.get_image = Mock()
        self.pepper.grow()
        self.pepper.art.get_image.assert_called_with('pepper3')

    @patch('pepper.pygame')
    def test_Pepper_is_harvestable_after_thirty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=30001)
        self.pepper.grow()
        self.assertEqual(self.pepper.harvestable, True)

#Test Tomatoes Here!
class test_Tomato(unittest.TestCase):

    def setUp(self):
        self.tomato = Tomato(50, 50)
        self.time = 0
        self.color = constants.GREEN

    def test_Tomato_can_be_created(self):
        self.assertTrue(True)

    @patch('tomato.pygame')
    def test_Tomato_changes_color_after_twenty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=30000)
        self.tomato.image = Mock()
        self.tomato.art = Mock()
        self.tomato.art.get_image = Mock()
        self.tomato.grow()
        self.tomato.art.get_image.assert_called_with('tomato2')

    @patch('tomato.pygame')
    def test_Tomato_is_eatable_after_twenty_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=30000)
        self.tomato.grow()
        self.assertEqual(self.tomato.eatable, True)

    @patch('tomato.pygame')
    def test_Tomato_changes_color_after_thirtyfive_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=40000)
        self.tomato.image = Mock()
        self.tomato.art = Mock()
        self.tomato.art.get_image = Mock()
        self.tomato.grow()
        self.tomato.art.get_image.assert_called_with('tomato3')

    @patch('tomato.pygame')
    def test_Tomato_is_harvestable_after_thirtyfive_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=40000)
        self.tomato.grow()
        self.assertEqual(self.tomato.harvestable, True)


#Test the Purse Here!
class test_Purse(unittest.TestCase):
    def setUp(self):
        self.purse = Purse()

    def test_Purse_can_be_created(self):
        self.assertTrue(True)

    def test_Purse_initial_money(self):
        self.assertEqual(0, self.purse.money)

    def test_canBuy_when_player_has_enough_money(self):
        self.purse.money = 10
        purchaseAmount = 10
        self.assertTrue(self.purse.canBuy(purchaseAmount))

    def test_canBuy_when_player_doesnt_have_enough_money(self):
        purchaseAmount = 1
        self.assertFalse(self.purse.canBuy(purchaseAmount))

    def test_Purse_money_is_subtracted_when_buying(self):
        self.purse.money = 11
        purchaseAmount = 10
        self.purse.buy(purchaseAmount)
        self.assertEqual(1, self.purse.money)

    def test_Purse_money_isnt_changed_when_cant_afford(self):
        purchaseAmount = 11
        self.purse.buy(purchaseAmount)
        self.assertEqual(0, self.purse.money)

    def test_Purse_money_added_after_selling(self):
        profit = 5
        self.purse.sell(profit)
        self.assertEqual(5, self.purse.money)

#Test the Title Screen!
class TestTitleScreen(unittest.TestCase):

    @patch('title_screen.pygame')
    def test_TitleScreen_can_be_created(self, mock_pygame):
        ts = TitleScreen()
        self.assertTrue(True)

    @patch('title_screen.pygame')
    def test_TitleScreen_draws_something(self, mock_pygame):
        ts = TitleScreen()
        mock_screen = Mock()
        ts.draw(mock_screen)
        self.assertTrue(mock_screen.blit.called, "Did not display text or image on the screen")

    @patch('title_screen.pygame')
    def test_TitleScreen_unloads_level_on_esc_keypress(self, mock_pygame):
        ts = TitleScreen()
        LevelManager().load_level(ts)
        event = Mock()
        event.type = mock_pygame.KEYDOWN
        event.key = mock_pygame.K_ESCAPE
        ts.handle_keyboard_event(event)

        self.assertIsNone(LevelManager().get_current_level())

#Test the Seed Bag!
class test_SeedBag(unittest.TestCase):

    def setUp(self):
        self.seedBag = SeedBag();

    def test_SeedBag_can_be_created(self):
        self.assertTrue(True)

    def test_SeedBag_number_of_carrot_seeds_changes_when_planted(self):
        self.seedBag.plantCarrotSeed()
        self.assertEqual(self.seedBag.numOfCarrotSeeds, 4)                   

    def test_SeedBag_number_of_cabbage_seeds_changes_when_planted(self):
        self.seedBag.plantCabbageSeed()
        self.assertEqual(self.seedBag.numOfCabbageSeeds, 4)

    def test_SeedBag_number_of_tomato_seeds_changes_when_planted(self):
        self.seedBag.plantTomatoSeed()
        self.assertEqual(self.seedBag.numOfTomatoSeeds, 4)

    def test_SeedBag_number_of_pepper_seeds_changes_when_planted(self):
        self.seedBag.plantPepperSeed()
        self.assertEqual(self.seedBag.numOfPepperSeeds, 4)

#Test the Trap!
class test_Trap(unittest.TestCase):

    def setUp(self):
        self.trap = Trap(50, 50);

    def test_Trap_can_be_created(self):
        self.assertTrue(True)

    @patch('trap.pygame')
    def test_Trap_is_kept_for_30_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=29999)
        trap_remove = self.trap.remove()
        self.assertEqual(trap_remove, True)

    @patch('trap.pygame')
    def test_Trap_is_removed_after_30_seconds(self, mock_pygame):
        mock_pygame.time.get_ticks = Mock(return_value=30001)
        trap_remove = self.trap.remove()
        self.assertEqual(trap_remove, True)

#Test the Trap Bag!
class test_TrapBag(unittest.TestCase):
    
    def setUp(self):
        self.trapBag = TrapBag()

    def test_TrapBag_can_be_created(self):
        self.assertTrue(True)

    def test_TrapBag_number_of_traps_changes_when_trap_is_set(self):
        self.trapBag.set_trap()
        self.assertEqual(self.trapBag.num_of_traps, 4)

    def test_TrapBag_can_only_set_traps_when_available(self):
        self.assertEqual(self.trapBag.can_set_trap(), True)

    def test_TrapBag_cannot_set_traps_when_none_available(self):
        trapBag = TrapBag()
        for x in range(0, 5):
            trapBag.set_trap()

        self.assertEqual(trapBag.can_set_trap(), False)

#Test the Player!
class test_Player(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_Player_can_be_created(self):
        self.assertTrue(True)

    def test_Player_moves_left_five_pixels(self):
        self.player.move_left()
        self.assertEqual(self.player.x_speed, -5)

    def test_Player_moves_right_five_pixels(self):
        self.player.move_right()
        self.assertEqual(self.player.x_speed, 5)

    def test_Player_moves_up_five_pixels(self):
        self.player.move_up()
        self.assertEqual(self.player.y_speed, -5)

    def test_Player_moves_down_five_pixels(self):
        self.player.move_down()
        self.assertEqual(self.player.y_speed, 5)

    def test_Player_plants_carrot_when_on_cycle_1(self):
        start_count = self.player.inventory.seedBag.numOfCarrotSeeds;
        self.player.selected = 1;
        self.player.plant(50, 50)
        self.assertEqual(self.player.inventory.seedBag.numOfCarrotSeeds, start_count - 1)

    def test_Player_plants_cabbage_when_on_cycle_2(self):
        start_count = self.player.inventory.seedBag.numOfCabbageSeeds;
        self.player.selected = 2;
        self.player.plant(50, 50)
        self.assertEqual(self.player.inventory.seedBag.numOfCabbageSeeds, start_count - 1)

    def test_Player_plants_pepper_when_on_cycle_3(self):
        start_count = self.player.inventory.seedBag.numOfPepperSeeds;
        self.player.selected = 3;
        self.player.plant(50, 50)
        self.assertEqual(self.player.inventory.seedBag.numOfPepperSeeds, start_count - 1)

    def test_Player_plants_tomato_when_on_cycle_4(self):
        start_count = self.player.inventory.seedBag.numOfTomatoSeeds;
        self.player.selected = 4;
        self.player.plant(50, 50)
        self.assertEqual(self.player.inventory.seedBag.numOfTomatoSeeds, start_count - 1)

    def test_Player_plants_trap_when_on_cycle_5(self):
        start_count = self.player.inventory.trapBag.num_of_traps;
        self.player.selected = 5;
        self.player.plant(50, 50)
        self.assertEqual(self.player.inventory.trapBag.num_of_traps, start_count - 1)

#Test the Rabbit!
class test_Rabbit(unittest.TestCase):
    
    def setUp(self):
        self.rabbit = Rabbit(50, 50)

    def test_Rabbit_can_be_created(self):
        self.assertTrue(True)

    #change health in rabbit
    def test_Rabbit_can_be_hurt(self):
        initial_health = self.rabbit.health
        self.rabbit.hurt_rabbit()
        self.assertEqual(self.rabbit.health, initial_health - 1)

    #make change in rabbit
    def test_Rabbit_can_set_health(self):
        self.rabbit.set_health(5)
        self.assertEqual(self.rabbit.health, 5)
        
#Test the Sound file!
class test_Sound(unittest.TestCase):
    
    def setUp(self):
        self.sound = Sound()

    def test_Sound_can_be_created(self):
        self.assertTrue(True)

    def test_Sound_can_get_attack_sound(self):
        self.assertEqual(self.sound.get_sound('attack'), self.sound._attack_sound)

    def test_Sound_can_get_money_sound(self):
        self.assertEqual(self.sound.get_sound('money'), self.sound._money)

    def test_Sound_can_get_background_music(self):
        self.assertEqual(self.sound.get_sound('background_music'), self.sound._background_music)

#Test the Inventory!
class test_Inventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()

    def test_Inventory_can_be_created(self):
        self.assertTrue(True)

#Test the Pixel!
class test_Pixel(unittest.TestCase):
    def setUp(self):
        self.pixel = Pixel()

    def test_Pixel_can_be_created(self):
        self.assertTrue(True)

    def test_Pixel_initial_positions(self):
        self.assertEqual(645, self.pixel.rect.x)
        self.assertEqual(420, self.pixel.rect.y)

    def test_Pixel_moves_left(self):
        self.pixel.move_left()
        self.pixel.update_position()
        self.assertEqual(-5, self.pixel.x_speed)
        self.assertEqual(640, self.pixel.rect.x)

    def test_Pixel_moves_right(self):
        self.pixel.move_right()
        self.pixel.update_position()
        self.assertEqual(5, self.pixel.x_speed)
        self.assertEqual(650, self.pixel.rect.x)

    def test_Pixel_moves_up(self):
        self.pixel.move_up()
        self.pixel.update_position()
        self.assertEqual(-5, self.pixel.y_speed)
        self.assertEqual(415, self.pixel.rect.y)

    def test_Pixel_moves_down(self):
        self.pixel.move_down()
        self.pixel.update_position()
        self.assertEqual(5, self.pixel.y_speed)
        self.assertEqual(425, self.pixel.rect.y)
    

#Run as main
if __name__ == '__main__':
    unittest.main()









        

        
