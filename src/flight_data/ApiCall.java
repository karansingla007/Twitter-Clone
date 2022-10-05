package flight_data;
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class ApiCall {
	private String apiUrl;
	
	ApiCall(String apiUrl) {
		this.apiUrl = apiUrl;
	}
	
	public void callApi() throws IOException {
		URL url = new URL(apiUrl);
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestProperty("Content-Type", "application/json");
		con.setRequestMethod("GET");
		con.setConnectTimeout(5000);
		int status = con.getResponseCode();

		Reader streamReader = null;

		if (status > 299) {
		    streamReader = new InputStreamReader(con.getErrorStream());
		} else {
		    streamReader = new InputStreamReader(con.getInputStream());
		}
		
		if(status == 200) {
			BufferedReader in = new BufferedReader(
					  new InputStreamReader(con.getInputStream()));
					String inputLine;
					StringBuffer content = new StringBuffer();
					while ((inputLine = in.readLine()) != null) {
					    content.append(inputLine);
					}
					in.close();
					System.out.print(content);
					
		}
		con.disconnect();
	}
}
