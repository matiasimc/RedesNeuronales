import Algebraic._
import org.scalatest._

class TreeEvaluateTest extends FlatSpec with Matchers {
  val tree = Plus(Id('x), Minus(Id('y), Id('z)))
  val ev = tree.evaluate(3,2,1)

  s"The tree" should "evaluate into 4" in {
    assert(ev == 4)
  }
}
