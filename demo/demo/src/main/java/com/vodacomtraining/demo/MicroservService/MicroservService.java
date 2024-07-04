package com.vodacomtraining.demo.MicroservService;

import com.vodacomtraining.demo.MicroservModel.MicroservModelProduct;
import com.vodacomtraining.demo.Repository.ProductRepository;
import jakarta.persistence.NoResultException;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MicroservService {

    @Autowired
    private ProductRepository productRepository;

    public List<MicroservModelProduct> getProducts(){
        return productRepository.findAll();
    }


    public MicroservModelProduct getProduct(int productId) {

        return productRepository.findById(productId).orElse(null);
    }

    public void deleteProduct(int productId){
        productRepository.deleteById(productId);
     }



    public void addProduct(MicroservModelProduct product){
        productRepository.save(product);
    }



    public void updateProduct(int productId, MicroservModelProduct product) {
        Optional<MicroservModelProduct> optional = productRepository.findById(productId);
        if (optional.isEmpty())
            throw new NoResultException("Product not found for the given id");
        var productFromDB = optional.get();
        BeanUtils.copyProperties(product, productFromDB, "productId");
        productRepository.save(productFromDB);
    }
}
