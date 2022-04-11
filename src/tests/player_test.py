import unittest
import game_logic.player as player1


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = player1.Player(64)

    def test_constructor(self):
        self.assertEqual(self.player.block_size, 64)

    def test_x_speed(self):
        self.assertEqual(self.player.speed_x, 64/6)

    def test_start_positioning_works(self):
        self.player.position_player_for_start(1080)
        self.assertTupleEqual(self.player.rect.topleft, (64*7, 1080-64))

    def test_start_positioning_workds_with_wrong_value(self):
        self.player.position_player_for_start(50)
        self.assertTupleEqual(self.player.rect.topleft, (0, 0))

    def test_player_jumps(self):
        self.player.jump()
        self.assertEqual(self.player.do_jump, True)

    def test_player_stops_jumping(self):
        self.player._jump_velocity_index = len(self.player.jump_velocities) -1
        self.player.jump()
        self.assertEqual(self.player.do_jump, False)
    
    def test_falling_velocity_index_works_when_falling(self):
        self.player.falling_status = True
        self.player.falling()
        self.assertEqual(self.player.falling_velocity_index, 1)

    def test_falling_velocity_index_works_when_not_falling(self):
        self.player.falling_status = False
        self.player.falling()
        self.assertEqual(self.player.falling_velocity_index, 0)

    def test_falling_velocity_index_doesnt_exceed_limit(self):
        self.player.falling_status = True
        answer = len(self.player.falling_velocities) - 1
        self.player.falling_velocity_index = answer
        self.player.falling()
        self.assertEqual(self.player.falling_velocity_index, answer)

    def test_next_position_while_falling_works(self):
        self.player.falling_velocity_index = 1
        outcome = self.player.next_position_while_falling()
        self.player.rect.x += self.player.speed_x
        self.player.rect.y += self.player.falling_velocities[self.player.falling_velocity_index]
        right_answer = self.player.rect
        self.assertEqual(outcome, right_answer)

    def test_update_function_with_when_given_values(self):
        self.player.update(10)
        self.assertEqual(self.player.rect.top, 10)
    
    def test_update_function_without_values(self):
        self.player.update()
        self.assertEqual(self.player.rect.top, 0)