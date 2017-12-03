import Arithmetic._
import org.scalatest._

class SelectionTest extends FlatSpec with Matchers {
  val trees : List[ArithmeticNode] = List.range(0, 50).map((x) => RandomArithmeticTree.generate(2))
  val selection = ArithmeticGenetics.arithmeticSelection(trees, 5, n => 3)
  s"The selection algorithm" should "select 5 trees " in {
    assert(5 == selection.length)
  }
  s"The selection algorithm" should "select trees in the original list" in {
    assert(selection.filter((n : ArithmeticNode) => trees.contains(n)) == selection)
  }

}

class CrossoverTest extends FlatSpec with Matchers {
  val trees : List[ArithmeticNode] = List.range(0, 50).map((x) => RandomArithmeticTree.generate(2))
  val crossover = ArithmeticGenetics.arithmeticCrossover(trees, 3)
  s"The crossover algorithm" should "generate 3 trees" in {
    assert(3 == crossover.length)
  }

}