package flight_data;
import java.net.HttpURLConnection;
import java.net.URLEncoder;
import java.net.URL;

import utils.Constants;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class ApiCall {
	private String baseUrl = Constants.baseUrl; 
	private String accessKey = Constants.accessKey;
	
	public ApiCall() {
		
	}
	
	public void callGetApi(String endPoint) throws IOException {
		String charset = "UTF-8";
		String queryParams = String.format("access_key=%s", URLEncoder.encode(accessKey, charset));
		
		URL url = new URL(baseUrl+endPoint+ "?"+queryParams);
		
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		con.setRequestProperty("Content-Type", "application/json");
		con.setRequestMethod("GET");
		con.setConnectTimeout(5000);
		con.setDoOutput(true);
		
		int status = con.getResponseCode();
		
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
					
		} else {
			System.out.print("error = "+ url);
		}
		con.disconnect();
	}
}
