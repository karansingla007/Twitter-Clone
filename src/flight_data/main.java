package flight_data;

public class main {

	public static void main(String[] args) {
		System.out.println("hello world");
		ApiCall apiCall = new ApiCall("https://reqres.in/api/users?page=2");
		try {
			apiCall.callApi();	
		} catch(Exception e) {
			System.out.print(e);
		}
		
	}
	
}
