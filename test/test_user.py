from unittest.mock import patch, Mock



def test_get_user_detail(self):
    with patch('my_module.connect_to_db', return_value=Mock()) as mock_db:
        mock_db.return_value.query_all_data.return_value = 'result data'
        # result = getUsersDetails()
        #
        # self.assertEqual(result, 'result data')
        # self.assertEqual(mock_db.call_count, 1)
        # self.assertEqual(mock_db.query_all_data.call_count, 1)