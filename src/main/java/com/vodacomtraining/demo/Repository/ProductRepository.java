package com.vodacomtraining.demo.Repository;

import com.vodacomtraining.demo.MicroservModel.MicroservModelProduct;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface ProductRepository extends CrudRepository<MicroservModelProduct, Integer> {

List<MicroservModelProduct> findAll();
}
