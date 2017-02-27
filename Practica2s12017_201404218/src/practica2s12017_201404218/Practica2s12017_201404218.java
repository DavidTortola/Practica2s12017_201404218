/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2s12017_201404218;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author David Tórtola
 */
public class Practica2s12017_201404218 {

    public static OkHttpClient webClient = new OkHttpClient();

    /**
     * @param args the command line arguments
     */
    public static Menu menu1 = new Menu();

    public static void main(String[] args) {
        // TODO code application logic here

        String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("kateleen", formBody);
        System.out.println(r + "---");

        menu1.setVisible(true);

    }

    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(practica2s12017_201404218.Practica2s12017_201404218.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(practica2s12017_201404218.Practica2s12017_201404218.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}
