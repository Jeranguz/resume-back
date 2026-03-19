from unittest.mock import patch, MagicMock
from lambda_function import lambda_handler
import json

def test_lambda_handler():
    # Mock the DynamoDB resource and table
    with patch('lambda_function.boto3.resource') as mock_db:
        mock_table = MagicMock()
        mock_db.return_value.Table.return_value = mock_table
        
        # Mock the response from update_item
        mock_table.update_item.return_value = {
            'Attributes': {
                'count': 42
            }
        }
        
        event = {} 
        context = None 
        response = lambda_handler(event, context)
        
        result = json.loads(response)
        assert result['statusCode'] == 200
        assert result['body'] == 42
        assert result['headers']['Access-Control-Allow-Origin'] == '*'