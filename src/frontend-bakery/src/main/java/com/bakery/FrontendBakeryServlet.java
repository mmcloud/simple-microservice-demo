package com.bakery;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * This servlet responses with "Hello World!" to GET requests.
 */
public class FrontendBakeryServlet extends HttpServlet {

	/**
	 * Write "Hello World!" to the response.
	 * 
	 * @param request
	 * @param response
	 * @throws ServletException
	 * @throws IOException
	 */
        @Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
            try (PrintWriter writer = response.getWriter()) {
                writer.println("Bakery");
            }
	}

}
