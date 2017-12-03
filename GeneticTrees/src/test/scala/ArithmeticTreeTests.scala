import Arithmetic._
import org.scalatest._

class TreeEvaluateTest1 extends FlatSpec with Matchers {
  val tree = Minus(Plus(Number(2), Number(3)), Number(5))
  s"The evaluation of the tree $tree" should "return 0" in {
    assert(tree.evaluate() == 0)
  }
}

class TreeEvaluateTest2 extends FlatSpec with Matchers {
  val tree = Div(Plus(Number(2), Number(3)), Number(5))
  s"The evaluation of the tree $tree" should "1" in {
    assert(tree.evaluate() == 1)
  }
}

class TreeEvaluateTest3 extends FlatSpec with Matchers {
  val tree = Number(14)
  s"The evaluation of the tree $tree" should "return 14" in {
    assert(tree.evaluate() == 14)
  }
}

class RandomGenerationTest extends FlatSpec with Matchers {
  val tree = RandomArithmeticTree.generate(5)
  //println("===Random Tree Generation===")
  //println(s"evaluation: ${tree.evaluate()}")
  //tree.prettyPrint()
  "The depth of the random generated tree" should "be 5" in {
    assert(5 == tree.height)
  }
}
