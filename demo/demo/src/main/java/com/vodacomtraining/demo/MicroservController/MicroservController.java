package com.vodacomtraining.demo.MicroservController;




import com.vodacomtraining.demo.MicroservModel.MicroservModelProduct;
import com.vodacomtraining.demo.MicroservService.MicroservService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;



@RestController
public class MicroservController {

    @Autowired
    private MicroservService microservService;

    @GetMapping("/products")
    public List<MicroservModelProduct> getProducts(){
        return microservService.getProducts();

    }

   @GetMapping("/products/{productId}")
    public MicroservModelProduct getProduct(@PathVariable int productId){
       MicroservModelProduct product = microservService.getProduct(productId);
       return product;
    }

    @DeleteMapping("/products/{productId}" )
    public void deleteProduct(@PathVariable int productId){
    microservService.deleteProduct(productId);
    }

    @PostMapping ("/products")
    public  void addProduct(@RequestBody MicroservModelProduct product){
        microservService.addProduct(product);
    }

    @PutMapping("/products/{productId}")
    public  void updateProduct(@RequestBody MicroservModelProduct product, @PathVariable int productId){
        microservService.updateProduct(productId, product);
    }

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*-------------------------------------------------------------------------------------------------------------------------------------*/








}

