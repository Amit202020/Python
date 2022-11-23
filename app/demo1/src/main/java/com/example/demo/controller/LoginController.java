package com.example.demo.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class LoginController {
	@RequestMapping(value = "/home", method = RequestMethod.GET)
	public ModelAndView loginpage1() {

		ModelAndView obj = new ModelAndView("LoginPage");
		return obj;

	}

	@RequestMapping(value = "/login", method = RequestMethod.POST)
	public ModelAndView logincheck(HttpServletRequest request) {

		String uid = request.getParameter("uid");
		String pass = request.getParameter("pass");

		//LoginService ls = new LoginService();
		//boolean b = ls.loginCheck(uid, pass);
		boolean b = true;
		if (b)
			return new ModelAndView("success");
		else
			return new ModelAndView("failure");
	}
}