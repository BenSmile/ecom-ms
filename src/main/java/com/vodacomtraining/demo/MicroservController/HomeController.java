package com.vodacomtraining.demo.MicroservController;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.util.Map;

@RestController
public class HomeController {

    @GetMapping
    Map<String, String> appInfo(){
        return Map.of("application name", "Product service", "time" , LocalDate.now().toString(), "zandi" , "mon bb Sophie et ma fille Celestes");
    }
}
