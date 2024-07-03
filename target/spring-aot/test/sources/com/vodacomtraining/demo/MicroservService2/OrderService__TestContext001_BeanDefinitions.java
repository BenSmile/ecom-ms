package com.vodacomtraining.demo.MicroservService2;

import com.vodacomtraining.demo.Repository.OrderRepository;
import com.vodacomtraining.demo.Repository.ProductRepository;
import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.aot.BeanInstanceSupplier;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;
import org.springframework.web.client.RestTemplate;

/**
 * Bean definitions for {@link OrderService}.
 */
@Generated
public class OrderService__TestContext001_BeanDefinitions {
  /**
   * Get the bean instance supplier for 'orderService'.
   */
  private static BeanInstanceSupplier<OrderService> getOrderServiceInstanceSupplier() {
    return BeanInstanceSupplier.<OrderService>forConstructor(OrderRepository.class, ProductRepository.class, RestTemplate.class)
            .withGenerator((registeredBean, args) -> new OrderService(args.get(0), args.get(1), args.get(2)));
  }

  /**
   * Get the bean definition for 'orderService'.
   */
  public static BeanDefinition getOrderServiceBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(OrderService.class);
    beanDefinition.setInstanceSupplier(getOrderServiceInstanceSupplier());
    return beanDefinition;
  }
}
