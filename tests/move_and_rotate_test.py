import unittest

class TestObjectMovement(unittest.TestCase):
    def test_movement_changes_position(self):
        obj = Movable_obj(12, 5, -7, 3)
        obj.move()
        self.assertEqual(obj.get_location(), (5, 8))

    def test_move_with_unreadable_position_raises_error(self):
        obj = Movable_obj(None, 5, -7, 3)
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot read position" in str(context.exception))

        obj = Movable_obj(12, None, -7, 3)
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot read position" in str(context.exception))

    def test_move_with_unreadable_velocity_raises_error(self):
        obj = Movable_obj(12, 5, None, 3)
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot read velocity" in str(context.exception))

        obj = Movable_obj(12, 5, -7, None)
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot read velocity" in str(context.exception))

    def test_move_with_unsettable_position_raises_error(self):
        obj = Movable_obj(12, 5, -7, 3)
        obj._x = None  # Simulate error condition for setting position
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot set position" in str(context.exception))

        obj = Movable_obj(12, 5, -7, 3)
        obj._y = None  # Simulate error condition for setting position
        with self.assertRaises(ValueError) as context:
            obj.move()
        self.assertTrue("Cannot set position" in str(context.exception))

class TestObjectRotate(unittest.Testcase):
    def test_rotate_changes_angle(self):
        obj = Rotatable_obj(3, 12)
        obj.rotate()
        self.assertEqual(obj.get_angle(), 15)

    def test_rotate_with_unreadable_angle_raises_error(self):
        obj = Rotatable_obj(None, 5)
        with self.assertRaises(ValueError) as context:
            obj.rotate()
        self.assertTrue("Cannot read angle" in str(context.exception))

    def test_rotate_with_unreadable_angVelocity_raises_error(self):
        obj = Rotatable_obj(5, None)
        with self.assertRaises(ValueError) as context:
            obj.rotate()
        self.assertTrue("Cannot read angVelocity" in str(context.exception))

if __name__ == '__main__':
    unittest.main()