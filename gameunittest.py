import unittest
import game


class TestHuntTheWumpus(unittest.TestCase):

    def setUp(self):
        game.start_game()

    def test_generate_map(self):
        game.generate_map()
        self.assertIn(0, game.rooms)
        self.assertIn(5, game.rooms)

    def test_start_game(self):
        game.start_game()
        self.assertIsNotNone(game.player_room)
        self.assertIsNotNone(game.wumpus_room)

    def test_move_player(self):
        current_room = game.player_room
        adjacent_room = game.rooms[current_room][0]
        game.move_player(adjacent_room)
        self.assertEqual(game.player_room, adjacent_room)

    def test_shoot_arrow(self):
        game.shoot_arrow(game.wumpus_room)
        self.assertTrue(game.has_won)

    def test_get_status(self):
        status = game.get_status()
        self.assertEqual(status["player_room"], game.player_room)
        self.assertIn("alive", status)
        self.assertIn("has_won", status)
        self.assertIn("adjacent_rooms", status)


if __name__ == "__main__":
    unittest.main()
