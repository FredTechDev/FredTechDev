```java
package io.github.yourusername;

import io.github.yourusername.skills.*;
import io.github.yourusername.interests.Coffee;

/**
 * Passionate Backend Developer specialized in building robust enterprise applications.
 * Focused on writing clean, maintainable, and highly efficient Java code.
 */
public class DeveloperProfile extends SoftwareEngineer implements Human {

    private final String name = "Your Name";
    private final String currentRole = "Backend Engineer";
    private final String location = "Your City, Country";
    
    // Core Engineering Tech Stack
    private final String[] languages = {"Java", "SQL", "Kotlin", "JavaScript"};
    private final String[] frameworks = {"Spring Boot", "Spring Cloud", "Hibernate", "JUnit5"};
    private final String[] cloudAndTools = {"Docker", "Kubernetes", "AWS", "Git", "Maven"};

    public DeveloperProfile() {
        super(YearsOfExperience.THREE_PLUS);
    }

    @Override
    public void run() {
        while (isAlive()) {
            keepCoding();
            drink(Coffee.BLACK);
        }
    }

    public void keepCoding() {
        System.out.println("Building scalable microservices...");
        System.out.println("Optimizing database queries...");
    }

    // Getters for recruiters
    public String getName() { return this.name; }
    public String getRole() { return this.currentRole; }
    public String[] getSkills() { return this.frameworks; }
}
```

### 🛠️ Metrics & Current Activity
<!-- Optional: Add dynamic cards below your code snippet to track your work -->

<p align="left">
  <img src="https://vercel.app" alt="Top Languages" />
  <img src="https://vercel.app" alt="GitHub Stats" />
</p>

### 📬 Connect With Me

* 💼 **LinkedIn:** [://linkedin.com](https://linkedin.com)
* 📧 **Email:** `your.email@example.com`
* 🌐 **Portfolio:** [yourwebsite.com](https://google.com)
