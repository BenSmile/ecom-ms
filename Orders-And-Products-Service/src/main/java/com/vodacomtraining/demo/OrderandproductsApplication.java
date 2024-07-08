package com.vodacomtraining.demo;

import com.vodacomtraining.demo.MicroservController.MicroservController;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class OrderandproductsApplication {

	public static void main(String[] args) {
		SpringApplication.run(OrderandproductsApplication.class, args);
		System.out.println("On démarre ici, c'est ma méthode main()!");
	}

	@Bean
	public RestTemplate restTemplate(){
		return new RestTemplate();
	}




}


