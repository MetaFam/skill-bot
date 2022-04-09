"use strict"

// import "https://d3js.org/d3.v7.min.js"

async function force_graph() {

  const personNodeSize = 10
  const skillNodeSize = 20
  const $ = {
    width: window.innerWidth - 100,
    height: window.innerHeight - 200,
    nodes: [],
    people: {},
    skills: {},
    links: [],
  }

  const svg = d3.select("#canvas")

  var peopleIndex = {}
  people.forEach((p) => {
    p.type = 'person'
    $.nodes.push(p)
    $.people[p.id] = p
  })

  var skillsIndex = {}
  skills.forEach((s) => {
    s.type = 'skill'
    $.nodes.push(s)
    $.skills[s.id] = s
  })

  people_skills.forEach((ps) => {

    var person = $.people[ps.person]
    var skill = $.skills[ps.skill]
    if (person && skill) {
      console.log("〈" + person.name + " ↔️ " + skill.name + "〉")
      ps.source = person
      ps.target = skill
      $.links.push(ps)
    } else {
      console.log("Broken link! " + ps.person + "(" + person + ") <-> " + ps.skill + "(" + skill + ")")
    }
  })

  function drag(simulation) {
    function dragstarted(event) {
      if (!event.active) simulation.alphaTarget(0.15).restart();
      event.subject.fx = event.subject.x;
      event.subject.fy = event.subject.y;
    }

    function dragged(event) {
      event.subject.fx = event.x;
      event.subject.fy = event.y;
    }

    function dragended(event) {
      if (!event.active) simulation.alphaTarget(alphaMin);
      event.subject.fx = null;
      event.subject.fy = null;
    }

    return d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);
  }


  const linkForce = d3
    .forceLink()
    .id(link => link.id)
    .strength(link => 0.2)
    .links($.links)

  const simulation = d3.forceSimulation()
    .force('link', linkForce)
    .force('attraction', d3.forceManyBody().strength(-100))
    .force('repulsion', d3.forceCollide(105))
    .force('center', d3.forceCenter($.width / 2, $.height / 2))

  simulation.stop()


    // simulation.stop()

  simulation.nodes($.nodes).on('tick', tick)

  function tick() {
    $.nodeElements
      .attr("cx", node => node.x)
      .attr("cy", node => node.y)
    $.textElements
      .attr("x", node => node.x)
      .attr("y", node => node.y)
    $.linkElements
      .attr('x1', link => link.source.x)
      .attr('y1', link => link.source.y)
      .attr('x2', link => link.target.x)
      .attr('y2', link => link.target.y)
  }

  svg
    .style("width", $.width + 'px')
    .style("height", $.height + 'px')

  $.linkElements = svg.append('g')
    .selectAll('line')
    .data($.links)
    .enter().append('line')
      .attr('class', "edge")

  $.nodeElements = svg.append('g')
    .selectAll('circle')
    .data($.nodes)
    .enter().append('circle')
      .attr('r', node => (node.type == "skill" ? skillNodeSize : personNodeSize ))
      .attr('class', node => "node " + node.type)
      .call(drag(simulation))

  $.textElements = svg.append('g')
    .selectAll('text')
    .data($.nodes)
    .enter().append('text')
      .text(node => node.name)
      .attr('dx', node => (node.type == "skill" ? skillNodeSize : personNodeSize ))
      .attr('dy', node => (node.type == "skill" ? -skillNodeSize : -personNodeSize ))
      .attr('class', node => "label " + node.type + "-label")

  simulation.alpha(0.25)
  simulation.restart()

  d3.select('#d3-canary')
    .text("✅ ");



}
