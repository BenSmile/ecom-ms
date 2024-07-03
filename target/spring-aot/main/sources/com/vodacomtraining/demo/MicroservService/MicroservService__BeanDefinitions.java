package com.vodacomtraining.demo.MicroservService;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.InstanceSupplier;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link MicroservService}.
 */
@Generated
public class MicroservService__BeanDefinitions {
  /**
   * Get the bean definition for 'microservService'.
   */
  public static BeanDefinition getMicroservServiceBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(MicroservService.class);
    InstanceSupplier<MicroservService> instanceSupplier = InstanceSupplier.using(MicroservService::new);
    instanceSupplier = instanceSupplier.andThen(MicroservService__Autowiring::apply);
    beanDefinition.setInstanceSupplier(instanceSupplier);
    return beanDefinition;
  }
}
