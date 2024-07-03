package com.vodacomtraining.demo.Repository;

import com.vodacomtraining.demo.MicroservModel.Order;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
}

