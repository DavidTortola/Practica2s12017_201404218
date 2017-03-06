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
 * @author Osmel David Tórtola Tistoj, Carné: 201404218
 */
public class Practica2s12017_201404218 {

    public static OkHttpClient webClient = new OkHttpClient();

    public static Menu menu1 = new Menu();

    //Método principal
    public static void main(String[] args) {
        menu1.setVisible(true);
    }

    //Método que conecta con el servidor de python
    public static String getString(String metodo, RequestBody formBody) {

        try {
            
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
            return response_string;
            
        } catch (MalformedURLException ex) {
            
            java.util.logging.Logger.getLogger(practica2s12017_201404218.Practica2s12017_201404218.class.getName()).log(Level.SEVERE, null, ex);
        
        } catch (Exception ex) {
         
            java.util.logging.Logger.getLogger(practica2s12017_201404218.Practica2s12017_201404218.class.getName()).log(Level.SEVERE, null, ex);
        
        }
        return null;
    }

}
