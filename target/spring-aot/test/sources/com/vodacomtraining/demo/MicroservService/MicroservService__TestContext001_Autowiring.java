package com.vodacomtraining.demo.MicroservService;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.aot.AutowiredFieldValueResolver;
import org.springframework.beans.factory.support.RegisteredBean;

/**
 * Autowiring for {@link MicroservService}.
 */
@Generated
public class MicroservService__TestContext001_Autowiring {
  /**
   * Apply the autowiring.
   */
  public static MicroservService apply(RegisteredBean registeredBean, MicroservService instance) {
    AutowiredFieldValueResolver.forRequiredField("productRepository").resolveAndSet(registeredBean, instance);
    return instance;
  }
}
