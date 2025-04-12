package com.foodychat.controller;

import RequestMapping.RequestMapping;

import RestController.RestController;
import model.User;
import service.UserService;

@RestController
@RequestMapping("/api/user")
public class UserController {
	package com.foodychat.controller;

	import org.springframework.stereotype.Controller;
	import org.springframework.web.bind.annotation.GetMapping;

	@Controller
	public class HomeController {

	    @GetMapping("/")
	    public String home() {
	        return "home";
	    }

	    @GetMapping("/login")
	    public String login() {
	        return "login";
	    }

	    @GetMapping("/signup")
	    public String signup() {
	        return "signup";
	    }

	    @GetMapping("/mypage")
	    public String mypage() {
	        return "mypage";
	    }

	    @GetMapping("/chatbot")
	    public String chatbot() {
	        return "chatbot";
	    }

	    @GetMapping("/image_upload")
	    public String imageUpload() {
	        return "image_upload";
	    }
	}