 import java.io.*;  
import java.io.IOException;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;  
import java.sql.*;  
@WebServlet("/ServletMySQL") 
public class ServletMySQL extends HttpServlet  
{    
        @Override
	public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException,ServletException 
      {  
         PrintWriter out = res.getWriter(); 
         res.setContentType("text/html");
         try 
         {  
            Class.forName("com.mysql.jdbc.Driver"); 
            Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/dbname", "username", "password");
            System.out.println("Connection Establisehd11");
             
            Statement stmt = c.createStatement();  
            ResultSet rs = stmt.executeQuery("select*from ebookshop;");
            out.println("<h1>Books Information :-</h1>");
            out.println("<table border=1 width=50% height=50%  >");  
            out.println("<tr><th>Book Id</th><th>Title</th><th>Author</th><th>Price</th><th>Quantity</th><tr>");  
            while (rs.next()) 
           {  
            	 int id=rs.getInt("book_id"); 
                 String n = rs.getString("book_title");  
                 String nm = rs.getString("book_author");  
                 int s = rs.getInt("book_price");   
                 int s1 = rs.getInt("quantity");
                 out.println("<tr><td>" + id + "</td><td>" + n + "</td><td>" + nm + "</td><td>" + s + "</td><td>" + s1 + "</td></tr>");
             }  
            out.println("</table>");  
            out.println("</html></body>");  
            c.close();  
            }  
             catch (Exception e) 
            {  
             out.println("error");  
         }  
     }  
 }  
