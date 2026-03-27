import React, { useState } from 'react';
import { 
  CheckCircle, 
  Clock, 
  AlertCircle, 
  Calendar, 
  User, 
  FileText, 
  ChevronRight,
  Layout,
  List,
  TrendingUp,
  Search
} from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

// --- DATA FROM PDF ---

const PROJECTS = [
  {
    id: 1,
    title: 'SDS Implementation',
    status: 'Near Completion',
    priority: 'High',
    owner: 'Mike',
    deadline: 'June 30 Cycle',
    description: 'Safety Data Sheets implementation. Will be offered free to all users (not just RTK) as a differentiator.',
    updates: [
      'Positioned as courtesy information, not comprehensive listing.',
      'System can identify when SDS was submitted by vendor.',
      'Team to follow up with vendors showing 100% noncompliance.'
    ],
    tags: ['Compliance', 'Vendor Mgmt']
  },
  {
    id: 2,
    title: 'Enhanced Descriptions via AI',
    status: 'Testing',
    priority: 'Medium',
    owner: 'Gerard',
    deadline: 'Next Week (Review)',
    description: 'AI-driven enhancement of search and requisition descriptions.',
    updates: [
      'Gerard reviewing descriptions across vendors/categories.',
      'Inconsistencies found between search and req descriptions.',
      'AI only modifies descriptions deemed unsatisfactory.',
      'Gerard to provide detailed findings in Excel.'
    ],
    tags: ['AI', 'UX']
  },
  {
    id: 3,
    title: 'Type-Ahead Functionality',
    status: 'Ready',
    priority: 'Low',
    owner: 'Dev Team',
    deadline: 'Immediate',
    description: 'Search prediction functionality ready to announce with other improvements.',
    updates: [],
    tags: ['UX', 'Search']
  },
  {
    id: 4,
    title: 'PO Print Updates (WebApper)',
    status: 'In Development',
    priority: 'High',
    owner: 'Dev Team',
    deadline: 'Early Feb',
    description: 'Refreshed interface with same flow/intuitiveness. Code completion targeted for end of Jan.',
    updates: [
      'Customer service training may be needed.'
    ],
    tags: ['Infrastructure', 'Training']
  },
  {
    id: 5,
    title: 'EPO Updates',
    status: 'Planned',
    priority: 'Medium',
    owner: 'Product',
    deadline: 'March',
    description: 'Updates for new fiscal year invoicing.',
    updates: [
      'Adding delivery information to comments.',
      'New queue option for vendors requiring invoicing after July 1st.',
      'Districts can create requisitions early and release on July 1.'
    ],
    tags: ['Fiscal', 'Features']
  }
];

const ACTION_ITEMS = [
  { id: 1, task: 'Verify SDS submissions included with bids', owner: 'Mike', status: 'Pending' },
  { id: 2, task: 'Provide detailed AI findings in Excel', owner: 'Gerard', status: 'Due Next Week' },
  { id: 3, task: 'Follow up with vendors (100% noncompliance)', owner: 'Team', status: 'Pending' },
  { id: 4, task: 'Customer Service Training for PO Print', owner: 'Training Lead', status: 'To Schedule' },
];

// --- COMPONENTS ---

const StatusBadge = ({ status }) => {
  const styles = {
    'Ready': 'bg-green-100 text-green-800 border-green-200',
    'Near Completion': 'bg-emerald-100 text-emerald-800 border-emerald-200',
    'Testing': 'bg-blue-100 text-blue-800 border-blue-200',
    'In Development': 'bg-indigo-100 text-indigo-800 border-indigo-200',
    'Planned': 'bg-slate-100 text-slate-800 border-slate-200',
  };
  return (
    <span className={`px-2.5 py-0.5 rounded-full text-xs font-medium border ${styles[status] || styles['Planned']}`}>
      {status}
    </span>
  );
};

const PriorityIcon = ({ priority }) => {
  if (priority === 'High') return <TrendingUp className="h-4 w-4 text-red-500" />;
  if (priority === 'Medium') return <TrendingUp className="h-4 w-4 text-orange-400" />;
  return <TrendingUp className="h-4 w-4 text-slate-400" />;
};

const ProjectCard = ({ project, onClick, isSelected }) => (
  <div 
    onClick={() => onClick(project)}
    className={`p-4 rounded-xl border transition-all cursor-pointer hover:shadow-md ${
      isSelected 
        ? 'bg-blue-50 border-blue-300 shadow-sm' 
        : 'bg-white border-slate-200'
    }`}
  >
    <div className="flex justify-between items-start mb-2">
      <StatusBadge status={project.status} />
      {project.deadline && (
        <span className="flex items-center text-xs text-slate-500">
          <Calendar className="h-3 w-3 mr-1" />
          {project.deadline}
        </span>
      )}
    </div>
    <h3 className="font-semibold text-slate-800 mb-1">{project.title}</h3>
    <p className="text-sm text-slate-500 line-clamp-2">{project.description}</p>
    
    <div className="mt-3 flex items-center justify-between">
      <div className="flex items-center">
        <div className="h-6 w-6 rounded-full bg-slate-200 flex items-center justify-center text-xs font-bold text-slate-600">
          {project.owner.charAt(0)}
        </div>
        <span className="ml-2 text-xs text-slate-600">{project.owner}</span>
      </div>
      <PriorityIcon priority={project.priority} />
    </div>
  </div>
);

const DetailView = ({ project }) => {
  if (!project) return (
    <div className="h-full flex flex-col items-center justify-center text-slate-400 bg-slate-50 rounded-xl border border-dashed border-slate-300 p-8">
      <Layout className="h-12 w-12 mb-4 opacity-50" />
      <p>Select a project to view details</p>
    </div>
  );

  return (
    <div className="bg-white rounded-xl border border-slate-200 shadow-sm h-full overflow-y-auto">
      <div className="p-6 border-b border-slate-100">
        <div className="flex justify-between items-start">
          <div>
             <StatusBadge status={project.status} />
             <h2 className="text-2xl font-bold text-slate-900 mt-2">{project.title}</h2>
          </div>
          <div className="text-right">
             <div className="text-sm text-slate-500">Target Date</div>
             <div className="font-semibold text-slate-800">{project.deadline}</div>
          </div>
        </div>
      </div>
      
      <div className="p-6 space-y-6">
        <div>
          <h3 className="text-sm font-semibold text-slate-900 uppercase tracking-wider mb-3 flex items-center">
            <FileText className="h-4 w-4 mr-2" />
            Description
          </h3>
          <p className="text-slate-600 leading-relaxed">{project.description}</p>
        </div>

        <div>
          <h3 className="text-sm font-semibold text-slate-900 uppercase tracking-wider mb-3 flex items-center">
            <List className="h-4 w-4 mr-2" />
            Key Updates & Notes
          </h3>
          <ul className="space-y-3">
            {project.updates.length > 0 ? (
              project.updates.map((update, idx) => (
                <li key={idx} className="flex items-start">
                  <span className="h-1.5 w-1.5 rounded-full bg-blue-500 mt-2 mr-3 flex-shrink-0" />
                  <span className="text-slate-600 text-sm">{update}</span>
                </li>
              ))
            ) : (
              <li className="text-slate-400 text-sm italic">No specific updates recorded.</li>
            )}
          </ul>
        </div>

        <div>
          <h3 className="text-sm font-semibold text-slate-900 uppercase tracking-wider mb-3 flex items-center">
            <User className="h-4 w-4 mr-2" />
            Owner
          </h3>
          <div className="flex items-center p-3 bg-slate-50 rounded-lg border border-slate-100">
            <div className="h-8 w-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 font-bold mr-3">
              {project.owner.charAt(0)}
            </div>
            <div>
              <div className="font-medium text-slate-900">{project.owner}</div>
              <div className="text-xs text-slate-500">Project Lead</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// --- MAIN APP ---

const App = () => {
  const [selectedProject, setSelectedProject] = useState(PROJECTS[0]);
  const [filter, setFilter] = useState('All');

  const filteredProjects = filter === 'All' 
    ? PROJECTS 
    : PROJECTS.filter(p => p.status.includes(filter) || p.priority === filter);

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-900 p-4 md:p-8">
      {/* Header */}
      <header className="max-w-7xl mx-auto mb-8 flex flex-col md:flex-row md:items-center justify-between">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">Project Planning & Priorities</h1>
          <p className="text-slate-500 mt-1 flex items-center">
            <Calendar className="h-4 w-4 mr-2" />
            Current Projects Through June 30th
          </p>
        </div>
        <div className="mt-4 md:mt-0 flex space-x-2">
          <div className="bg-white px-3 py-2 rounded-lg border border-slate-200 flex items-center shadow-sm">
            <Clock className="h-4 w-4 text-slate-400 mr-2" />
            <span className="text-sm font-medium">Q1-Q2 Focus</span>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Column: Project List (4 cols) */}
        <div className="lg:col-span-4 space-y-4">
          <div className="flex items-center justify-between mb-2">
            <h2 className="font-bold text-slate-700">Initiatives</h2>
            <span className="text-xs font-medium bg-slate-200 text-slate-600 px-2 py-1 rounded-full">{filteredProjects.length}</span>
          </div>
          
          {/* Filters (Simple) */}
          <div className="flex space-x-2 overflow-x-auto pb-2">
            {['All', 'High', 'Medium'].map(f => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${
                  filter === f ? 'bg-slate-800 text-white' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'
                }`}
              >
                {f}
              </button>
            ))}
          </div>

          <div className="space-y-3">
            {filteredProjects.map(project => (
              <ProjectCard 
                key={project.id} 
                project={project} 
                onClick={setSelectedProject}
                isSelected={selectedProject?.id === project.id}
              />
            ))}
          </div>
        </div>

        {/* Middle Column: Detail View (5 cols) */}
        <div className="lg:col-span-5 h-[600px]">
          <DetailView project={selectedProject} />
        </div>

        {/* Right Column: Action Items & Summary (3 cols) */}
        <div className="lg:col-span-3 space-y-6">
          
          {/* Action Items Widget */}
          <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
            <h3 className="font-bold text-slate-800 mb-4 flex items-center">
              <AlertCircle className="h-5 w-5 text-orange-500 mr-2" />
              Action Items
            </h3>
            <div className="space-y-4">
              {ACTION_ITEMS.map(item => (
                <div key={item.id} className="flex items-start group">
                  <div className="mt-0.5 mr-3">
                    <div className="h-4 w-4 rounded border border-slate-300 group-hover:border-blue-500 transition-colors" />
                  </div>
                  <div>
                    <p className="text-sm text-slate-700 leading-snug">{item.task}</p>
                    <div className="flex items-center mt-1">
                       <span className="text-[10px] font-bold text-slate-500 bg-slate-100 px-1.5 py-0.5 rounded uppercase mr-2">{item.owner}</span>
                       <span className="text-[10px] text-orange-600 font-medium">{item.status}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Quick Stats */}
          <div className="bg-slate-900 rounded-xl shadow-sm p-5 text-white">
            <h3 className="font-bold mb-4">Milestone Summary</h3>
            <div className="space-y-4 relative">
              <div className="absolute left-[7px] top-2 bottom-2 w-0.5 bg-slate-700" />
              
              <div className="relative flex items-center">
                <div className="h-4 w-4 rounded-full bg-green-500 border-2 border-slate-900 z-10" />
                <div className="ml-4">
                  <div className="text-xs text-slate-400">Now</div>
                  <div className="text-sm font-medium">SDS & Type-Ahead</div>
                </div>
              </div>

              <div className="relative flex items-center">
                <div className="h-4 w-4 rounded-full bg-blue-500 border-2 border-slate-900 z-10" />
                <div className="ml-3">
                  <div className="text-xs text-slate-400">Early Feb</div>
                  <div className="text-sm font-medium">PO Print (WebApper)</div>
                </div>
              </div>

              <div className="relative flex items-center">
                <div className="h-4 w-4 rounded-full bg-slate-500 border-2 border-slate-900 z-10" />
                <div className="ml-4">
                  <div className="text-xs text-slate-400">March</div>
                  <div className="text-sm font-medium">EPO Updates</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default App;