package flight_data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import utils.Constants;

public class main {

	public static void main(String[] args) {
		System.out.println("hello world");
		ApiCall apiCall = new ApiCall();
		try {
//			apiCall.callGetApi("v1/flights");
			Connection connection = DriverManager.getConnection(Constants.jbcUrl);
			
			String sql = "Select * from flightData";
			Statement statement = connection.createStatement();
			ResultSet resultSet = statement.executeQuery(sql);
			
			System.out.print(resultSet);
		} catch(Exception e) {
			System.out.print(e);
		}
		
	}
	
}
