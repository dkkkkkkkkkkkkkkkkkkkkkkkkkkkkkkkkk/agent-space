import { useEffect, useState } from 'react'

import api from './api/client'

function App() {
  const [me, setMe] = useState(null)
  const [agents, setAgents] = useState([])
  const [tasks, setTasks] = useState([])
  const [workflows, setWorkflows] = useState([])

  useEffect(() => {
    const loadData = async () => {
      try {
        const [meRes, agentsRes, tasksRes, workflowsRes] = await Promise.all([
          api.get('/me'),
          api.get('/agents'),
          api.get('/tasks'),
          api.get('/workflows'),
        ])

        setMe(meRes.data)
        setAgents(agentsRes.data)
        setTasks(tasksRes.data)
        setWorkflows(workflowsRes.data)
      } catch (err) {
        console.log('No auth session yet. Login to continue.')
      }
    }

    loadData()
  }, [])

  const loginDemo = async () => {
    try {
      const form = new URLSearchParams()
      form.append('username', 'demo@agentspace.ai')
      form.append('password', 'demo123')

      const res = await api.post('/login', form, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      })

      localStorage.setItem('token', res.data.access_token)
      window.location.reload()
    } catch (err) {
      console.error('Login failed', err)
    }
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Agent Space</p>
          <h1>Operations dashboard</h1>
        </div>

        <button className="primary-btn" onClick={loginDemo}>Demo Login</button>
      </header>

      <div className="stats-grid">
        <div className="stat-card">
          <span>Total agents</span>
          <strong>{agents.length}</strong>
        </div>
        <div className="stat-card">
          <span>Open tasks</span>
          <strong>{tasks.filter((task) => task.status !== 'completed').length}</strong>
        </div>
        <div className="stat-card">
          <span>Workflows</span>
          <strong>{workflows.length}</strong>
        </div>
        <div className="stat-card">
          <span>User</span>
          <strong>{me?.username || 'Guest'}</strong>
        </div>
      </div>

      <div className="grid-two">
        <section className="panel">
          <h2>Agent list</h2>
          {agents.length === 0 ? (
            <p className="placeholder">No agents created yet.</p>
          ) : (
            <ul className="list">
              {agents.map((agent) => (
                <li key={agent.id}>
                  <div>
                    <strong>{agent.name}</strong>
                    <span>{agent.description || 'No description'}</span>
                  </div>
                  <em>{agent.status}</em>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section className="panel">
          <h2>Task queue</h2>
          {tasks.length === 0 ? (
            <p className="placeholder">No tasks available.</p>
          ) : (
            <ul className="list">
              {tasks.map((task) => (
                <li key={task.id}>
                  <div>
                    <strong>{task.title}</strong>
                    <span>{task.description || 'No description'}</span>
                  </div>
                  <em>{task.status}</em>
                </li>
              ))}
            </ul>
          )}
        </section>
      </div>

      <section className="panel">
        <h2>Workflow library</h2>
        {workflows.length === 0 ? (
          <p className="placeholder">No workflows defined.</p>
        ) : (
          <ul className="list workflow-list">
            {workflows.map((workflow) => (
              <li key={workflow.id}>
                <div>
                  <strong>{workflow.name}</strong>
                  <span>{workflow.prompt}</span>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  )
}

export default App
