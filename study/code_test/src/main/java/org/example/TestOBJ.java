package org.example;

public class TestOBJ implements Cloneable{

    private String name;
    private int age;

    public TestOBJ() {

    }
    public TestOBJ(String name, int age) {
        this.name = name;
        this.age = age;
    }
    @Override
    public TestOBJ clone() throws CloneNotSupportedException {
        return (TestOBJ) super.clone();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "TestOBJ{" +
                "name='" + name + '\'' +
                ", age=" + age + '\'' +
                ", identityHashCode= " + System.identityHashCode(this) +
                '}';
    }
}
